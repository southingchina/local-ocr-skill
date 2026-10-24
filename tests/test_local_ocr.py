import base64
import json
import sys
import tempfile
import threading
import unittest
from unittest import mock
from contextlib import redirect_stdout
import io
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import local_ocr


class LocalOcrTests(unittest.TestCase):
    def test_cli_forwards_configurable_engine_options(self):
        with mock.patch.object(local_ocr, "ocr_image", return_value={"code": 100, "data": "ok"}) as call:
            with redirect_stdout(io.StringIO()):
                self.assertEqual(local_ocr.main(["sample.png", "--umi-exe", "engine.exe", "--endpoint", "http://localhost:1224/api/ocr", "--no-start", "--output", str(Path(tempfile.gettempdir()) / "local-ocr-cli-test.txt")]), 0)
            self.assertEqual(call.call_args.kwargs["endpoint"], "http://localhost:1224/api/ocr")
            self.assertEqual(call.call_args.kwargs["executable"], Path("engine.exe"))
            self.assertFalse(call.call_args.kwargs["start_if_needed"])

    def test_extract_text_preserves_engine_line_endings(self):
        response = {
            "code": 100,
            "data": [
                {"text": "第一段", "end": "\n"},
                {"text": "第二段", "end": ""},
            ],
        }
        self.assertEqual(local_ocr.extract_text(response), "第一段\n第二段")

    def test_ocr_image_posts_local_bytes_and_layout_options(self):
        received = {}

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *_args):
                return

            def do_POST(self):
                length = int(self.headers["Content-Length"])
                received.update(json.loads(self.rfile.read(length)))
                body = json.dumps({"code": 100, "data": "识别成功"}, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        server = HTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            with tempfile.TemporaryDirectory() as folder:
                image = Path(folder) / "中文 图片.png"
                image.write_bytes(b"fake-png")
                result = local_ocr.ocr_image(
                    image,
                    endpoint=f"http://127.0.0.1:{server.server_port}/api/ocr",
                    layout="single_para",
                    max_side_len=2880,
                    start_if_needed=False,
                )
            self.assertEqual(result["data"], "识别成功")
            self.assertEqual(base64.b64decode(received["base64"]), b"fake-png")
            self.assertEqual(received["options"]["tbpu.parser"], "single_para")
            self.assertEqual(received["options"]["ocr.limit_side_len"], 2880)
            self.assertEqual(received["options"]["data.format"], "text")
        finally:
            server.shutdown()
            server.server_close()

    def test_refuses_to_send_images_to_a_non_loopback_endpoint(self):
        with tempfile.TemporaryDirectory() as folder:
            image = Path(folder) / "private.png"
            image.write_bytes(b"private-image")
            with self.assertRaisesRegex(ValueError, "loopback"):
                local_ocr.ocr_image(
                    image,
                    endpoint="https://example.com/api/ocr",
                    start_if_needed=False,
                )


if __name__ == "__main__":
    unittest.main()
