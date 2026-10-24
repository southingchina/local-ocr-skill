#!/usr/bin/env python3
"""Run the installed Umi-OCR engine through its loopback-only HTTP API."""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_ENDPOINT = "http://127.0.0.1:1224/api/ocr"
DEFAULT_UMI_EXE = Path(os.environ.get("UMI_OCR_EXE") or shutil.which("Umi-OCR.exe") or "Umi-OCR.exe")
LOOPBACK_HOSTS = {"127.0.0.1", "localhost", "::1"}


def extract_text(response: dict) -> str:
    code = response.get("code")
    data = response.get("data")
    if code == 101:
        return ""
    if code != 100:
        raise RuntimeError(f"OCR failed with code {code}: {data}")
    if isinstance(data, str):
        return data
    if isinstance(data, list):
        return "".join(f"{item.get('text', '')}{item.get('end', '')}" for item in data)
    raise RuntimeError("OCR returned an unsupported result format")


def _post_json(endpoint: str, payload: dict, timeout: float) -> dict:
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def _start_umi(executable: Path) -> None:
    if not executable.is_file():
        raise FileNotFoundError(f"Umi-OCR executable not found: {executable}")
    creationflags = 0
    startupinfo = None
    if sys.platform == "win32":
        creationflags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
    subprocess.Popen(
        [str(executable), "--hide"],
        cwd=str(executable.parent),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creationflags,
        startupinfo=startupinfo,
        close_fds=True,
    )


def ocr_image(
    image_path: str | Path,
    *,
    endpoint: str = DEFAULT_ENDPOINT,
    layout: str = "multi_para",
    max_side_len: int = 2880,
    result_format: str = "text",
    start_if_needed: bool = True,
    executable: str | Path = DEFAULT_UMI_EXE,
    timeout: float = 60,
) -> dict:
    parsed = urlparse(endpoint)
    if parsed.hostname not in LOOPBACK_HOSTS:
        raise ValueError("OCR endpoint must use a loopback address")
    image = Path(image_path).resolve()
    if not image.is_file():
        raise FileNotFoundError(f"Image not found: {image}")
    payload = {
        "base64": base64.b64encode(image.read_bytes()).decode("ascii"),
        "options": {
            "ocr.language": "models/config_chinese.txt",
            "ocr.cls": True,
            "ocr.limit_side_len": max_side_len,
            "tbpu.parser": layout,
            "tbpu.ignoreArea": [],
            "data.format": result_format,
        },
    }
    try:
        return _post_json(endpoint, payload, timeout)
    except (urllib.error.URLError, ConnectionError):
        if not start_if_needed:
            raise
    _start_umi(Path(executable))
    deadline = time.monotonic() + 20
    last_error: Exception | None = None
    while time.monotonic() < deadline:
        try:
            return _post_json(endpoint, payload, timeout)
        except (urllib.error.URLError, ConnectionError) as error:
            last_error = error
            time.sleep(0.5)
    raise RuntimeError("Umi-OCR did not become ready within 20 seconds") from last_error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline OCR using the local Umi-OCR Paddle engine")
    parser.add_argument("image", type=Path)
    parser.add_argument("--layout", choices=("multi_para", "multi_line", "single_para", "single_line", "single_code", "none"), default="multi_para")
    parser.add_argument("--max-side", type=int, choices=(960, 2880, 4320, 999999), default=2880)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT, help="Loopback Umi-OCR API URL")
    parser.add_argument("--umi-exe", type=Path, default=DEFAULT_UMI_EXE, help="Umi-OCR executable path")
    parser.add_argument("--no-start", action="store_true", help="Do not start Umi-OCR automatically")
    args = parser.parse_args(argv)

    api_format = "dict" if args.format == "json" else "text"
    response = ocr_image(args.image, endpoint=args.endpoint, executable=args.umi_exe, start_if_needed=not args.no_start, layout=args.layout, max_side_len=args.max_side, result_format=api_format)
    output = json.dumps(response, ensure_ascii=False, indent=2) if args.format == "json" else extract_text(response)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
