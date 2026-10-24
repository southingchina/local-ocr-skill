# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

画像から文字を抽出する Umi-OCR のローカル HTTP クライアントと、明示的に呼び出す Codex Skill です。段落やコードのレイアウト、画像サイズを選択し、テキストまたは構造化 JSON を出力できます。接続先はループバックアドレスに限定されます。Python 側は標準ライブラリのみを使用します。Umi-OCR と言語モデルを別途導入し、HTTP API を有効にしてください。

## 必要な環境

Python 3.10+; Umi-OCR HTTP API

## 設定とエントリーポイント

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## 導入と使用方法

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


## 公開範囲と制限

既定の API は http://127.0.0.1:1224/api/ocr です。Windows で非表示起動するには UMI_OCR_EXE または --umi-exe を指定し、起動済みのエンジンを使う場合は --no-start を指定します。--endpoint で外部サーバーは選択できません。精度、表、読み順はエンジンに依存するため確認が必要です。エンジン、モデル、個人画像、クラウドへの切り替え機能は含みません。スキャン PDF は先に画像化してください。

## 検証記録

2026-10-24 · Python: 4 ✓

## ライセンスと出典

[MIT](LICENSE)

これらは文書の言語版です。アプリ画面、CLI 出力、実行ファイルは現在の実装に従います。

[中国語の詳細リファレンス](README.zh-CN.md) · [言語版の保守方針](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — 再現できる問題は合成データで報告し、ログの認証情報や個人情報を除いてください。
