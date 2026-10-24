# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

Lokaler HTTP-Client für Umi-OCR und ausdrücklich aufzurufender Codex-Skill zur Texterkennung in Bildern. Absatz- oder Code-Layout, Bildgröße sowie Text- oder strukturierte JSON-Ausgabe sind wählbar. Der Client akzeptiert ausschließlich Loopback-Adressen. Python verwendet nur die Standardbibliothek; Umi-OCR und Sprachmodelle werden separat installiert und die HTTP-API muss aktiviert werden.

## Voraussetzungen

Python 3.10+; Umi-OCR HTTP API

## Konfiguration und Einstiegspunkte

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## Installation und Verwendung

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


## Umfang und Einschränkungen

Die Standard-API ist http://127.0.0.1:1224/api/ocr. Für den versteckten Windows-Start UMI_OCR_EXE oder --umi-exe setzen; bei laufender Engine --no-start verwenden. --endpoint erlaubt keinen entfernten Server. Erkennungsgenauigkeit, Tabellen und Lesereihenfolge hängen von der Engine ab und müssen geprüft werden. Engine, Modelle, private Bilder und Cloud-Fallback sind nicht enthalten. Gescannte PDF-Seiten zuerst in Bilder umwandeln.

## Prüfstand

2026-10-24 · Python: 4 ✓

## Lizenz und Herkunft

[MIT](LICENSE)

Dies sind Sprachfassungen der Dokumentation. Oberflächen, CLI-Ausgaben und ausführbare Pakete folgen weiterhin der aktuellen Implementierung.

[Vollständige chinesische Referenz](README.zh-CN.md) · [Pflege der Sprachfassungen](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — Reproduzierbare Probleme mit synthetischen Daten melden. Zugangsdaten und private Informationen aus Protokollen entfernen.
