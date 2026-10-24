# Local OCR Skill · 本地图片转文字

通过 **Umi-OCR 的本地 HTTP API** 提取图片文字。支持文本或 JSON 输出、布局模式及坐标/置信度数据。脚本只允许回环地址，图片不会被这个客户端发送到远端 OCR 服务。

## 安装

需要 Python 3.10+（标准库）以及单独安装的 [Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)。启用其 HTTP API，默认监听 `127.0.0.1:1224`。本仓库不包含 OCR 引擎、模型或第三方二进制。

```shell
git clone https://github.com/southingchina/local-ocr-skill.git
cd local-ocr-skill
python scripts/local_ocr.py ./example.png --no-start
python scripts/local_ocr.py ./example.png --layout single_para --format json --output ./result.json --no-start
```

### Windows 自动启动引擎

```powershell
$env:UMI_OCR_EXE = 'C:\Tools\Umi-OCR\Umi-OCR.exe'
python scripts/local_ocr.py .\example.png
```

也可传 `--umi-exe`。引擎未启动且找不到可执行文件时会明确报错，不回退到云服务。已启动的引擎可跨系统调用；隐藏启动逻辑主要面向 Windows。

## 参数

| 参数 | 用途 |
| --- | --- |
| `--layout` | `multi_para` 默认；另有 `single_para`、`single_code`、`none` 等 |
| `--max-side` | OCR 最大边长，默认 2880，可选 960/4320/999999 |
| `--format text/json` | 纯文字或保留引擎返回的结构化结果 |
| `--endpoint` | 自定义回环 API 地址；远端地址会被拒绝 |
| `--no-start` | 禁止自动启动引擎 |
| `--output` | 将结果写入文件 |

在 Codex 中可将仓库安装为 `local-ocr` Skill，默认显式调用；单纯提供截图不会自动启动本地 OCR。扫描 PDF 请先自行按需要渲染成图片。

## 验证与限制

```shell
python -m unittest discover -s tests -v
```

自动测试验证文本拼接、本地 HTTP 请求和远端地址拒绝；不代表已在所有引擎版本、版式或语言上测量准确率。文字、表格和阅读顺序仍取决于 Umi-OCR 的实际输出。依赖引擎的 HTTP 配置与语言模型，复杂版式需要人工复核。

本项目为独立 API 客户端与助手 Skill，MIT。Umi-OCR 及模型按其自身许可证分发，不包含在本仓库内。
