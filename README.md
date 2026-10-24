# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

A local Umi-OCR HTTP client and explicitly invoked Codex Skill for extracting text from images. Choose paragraph or code layouts, adjust image size, and export plain text or structured JSON. The client accepts loopback endpoints only. Python uses its standard library; install Umi-OCR and its language models separately, then enable its HTTP API.

## Requirements

Python 3.10+; Umi-OCR HTTP API

## Configuration and entry points

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## Installation and usage

```shell
git clone https://github.com/southingchina/local-ocr-skill.git
cd local-ocr-skill
python scripts/local_ocr.py ./example.png --no-start
python scripts/local_ocr.py ./example.png --layout single_para --format json --output ./result.json --no-start
```


```powershell
$env:UMI_OCR_EXE = 'C:\Tools\Umi-OCR\Umi-OCR.exe'
python scripts/local_ocr.py .\example.png
```


```shell
python -m unittest discover -s tests -v
```


## Scope and limitations

The default API is http://127.0.0.1:1224/api/ocr. Set UMI_OCR_EXE or --umi-exe for hidden startup on Windows, or use --no-start with a running engine. --endpoint cannot select a remote server. JSON preserves the engine's structure; accuracy, tables and reading order still depend on the engine and require review. The package contains no engine, models, private images or cloud fallback. Render scanned PDF pages to images first.

## Validation record

2026-10-24 · Python: 4 ✓

## License and attribution

[MIT](LICENSE)

These are documentation editions. Application interfaces, CLI output and executable releases retain the behavior of the current implementation.

[Complete Chinese reference](README.zh-CN.md) · [Language maintenance policy](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — Report a reproducible issue with synthetic data. Remove credentials and private information from logs.
