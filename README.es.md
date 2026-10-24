# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

Cliente HTTP local de Umi-OCR y Skill de Codex de invocación explícita para extraer texto de imágenes. Permite elegir distribuciones de párrafos o código, ajustar el tamaño y exportar texto o JSON estructurado. Solo acepta direcciones de bucle local. Python utiliza su biblioteca estándar; instala Umi-OCR y sus modelos de idioma por separado y activa su API HTTP.

## Requisitos

Python 3.10+; Umi-OCR HTTP API

## Configuración y puntos de entrada

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## Instalación y uso

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


## Alcance y limitaciones

La API predeterminada es http://127.0.0.1:1224/api/ocr. Define UMI_OCR_EXE o --umi-exe para iniciar el motor oculto en Windows, o usa --no-start si ya está en ejecución. --endpoint no admite servidores remotos. La precisión, las tablas y el orden de lectura dependen del motor y requieren revisión. No se incluyen el motor, modelos, imágenes privadas ni una alternativa en la nube. Convierte primero las páginas PDF escaneadas en imágenes.

## Registro de validación

2026-10-24 · Python: 4 ✓

## Licencia y atribución

[MIT](LICENSE)

Son versiones de la documentación. Las interfaces, salidas CLI y ejecutables mantienen el comportamiento de la implementación actual.

[Referencia completa en chino](README.zh-CN.md) · [Política de mantenimiento de idiomas](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — Comunica problemas reproducibles con datos sintéticos. Elimina credenciales e información privada de los registros.
