---
name: local-ocr
description: Use only when the user explicitly asks to call or use the local OCR tool, or explicitly invokes $local-ocr for a local image, screenshot, scan, photographed document, or image-based PDF.
---

# Local OCR

Activate this skill only after an explicit request to use local OCR. Receiving a screenshot or a request such as “看看这是什么情况”, “读取这张图”, “提取图片文字”, or “帮我看截图” does not activate it by itself. Use normal image inspection for those requests.

Use the installed Umi-OCR Paddle engine as the first text-extraction pass. It runs locally and keeps image bytes on loopback. Use visual inspection afterward for layout interpretation and uncertain characters.

## Run

```powershell
python scripts/local_ocr.py "C:\images\sample.png" --layout multi_para
```

The helper reuses `http://127.0.0.1:1224`. Set `UMI_OCR_EXE` or `--umi-exe` for hidden startup; use `--no-start` for an already running engine. Resolve script paths relative to this Skill directory.

Choose layout by source:

| Source | Option |
|---|---|
| ordinary screenshot or mixed columns | `--layout multi_para` |
| one continuous document column | `--layout single_para` |
| code screenshot | `--layout single_code` |
| preserve raw blocks for manual ordering | `--layout none --format json` |
| very small text or large scan | add `--max-side 4320` |

Use `--format json` when coordinates, confidence, columns, tables, or reading order need inspection. Use `--output <path>` for long results.

## Delivery

Preserve wording, numbers, punctuation, paragraphs, and visible order. Check low-confidence text and dense layouts against the source image. Mark unreadable content as `[无法辨认]`; do not silently invent missing characters.

For a scanned PDF, render the needed pages to images with the PDF workflow, then run this helper on those images. Use a document parser such as MinerU only when tables, formulas, or page structure matter more than plain transcription.

## Boundaries

This skill is for textual content. Use normal image inspection when the task concerns visual style, objects, colors, or composition. The helper rejects non-loopback OCR endpoints so local images are not uploaded.
