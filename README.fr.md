# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

Client HTTP local d'Umi-OCR et Skill Codex à invocation explicite pour extraire le texte des images. Choisissez la disposition des paragraphes ou du code, la taille d'image et une sortie texte ou JSON structuré. Seules les adresses de bouclage sont acceptées. Python utilise sa bibliothèque standard ; installez séparément Umi-OCR et ses modèles linguistiques, puis activez son API HTTP.

## Prérequis

Python 3.10+; Umi-OCR HTTP API

## Configuration et points d’entrée

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## Installation et utilisation

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


## Périmètre et limites

L'API par défaut est http://127.0.0.1:1224/api/ocr. Définissez UMI_OCR_EXE ou --umi-exe pour un démarrage masqué sous Windows, ou utilisez --no-start avec un moteur déjà lancé. --endpoint n'accepte pas de serveur distant. La précision, les tableaux et l'ordre de lecture dépendent du moteur et doivent être vérifiés. Le paquet ne contient ni moteur, ni modèles, ni images privées, ni basculement vers le cloud. Convertissez d'abord les pages PDF numérisées en images.

## Historique de validation

2026-10-24 · Python: 4 ✓

## Licence et attribution

[MIT](LICENSE)

Il s’agit de versions de la documentation. Interfaces, sorties CLI et exécutables conservent le comportement de l’implémentation actuelle.

[Référence complète en chinois](README.zh-CN.md) · [Politique de maintenance des langues](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — Signalez les problèmes reproductibles avec des données synthétiques. Retirez identifiants secrets et informations privées des journaux.
