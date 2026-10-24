# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

Cliente HTTP local do Umi-OCR e Skill do Codex com invocação explícita para extrair texto de imagens. Permite escolher layouts de parágrafos ou código, ajustar o tamanho e exportar texto ou JSON estruturado. Aceita somente endereços de loopback. O código Python usa a biblioteca padrão; instale o Umi-OCR e seus modelos de idioma separadamente e ative a API HTTP.

## Requisitos

Python 3.10+; Umi-OCR HTTP API

## Configuração e pontos de entrada

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## Instalação e uso

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


## Escopo e limitações

A API padrão é http://127.0.0.1:1224/api/ocr. Defina UMI_OCR_EXE ou --umi-exe para iniciar o mecanismo oculto no Windows, ou use --no-start se ele já estiver aberto. --endpoint não aceita servidores remotos. Precisão, tabelas e ordem de leitura dependem do mecanismo e precisam de revisão. O pacote não inclui mecanismo, modelos, imagens privadas ou alternativa na nuvem. Converta primeiro as páginas de PDF digitalizadas em imagens.

## Registro de validação

2026-10-24 · Python: 4 ✓

## Licença e créditos

[MIT](LICENSE)

São versões da documentação. Interfaces, saídas CLI e executáveis mantêm o comportamento da implementação atual.

[Referência completa em chinês](README.zh-CN.md) · [Política de manutenção dos idiomas](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — Relate problemas reproduzíveis com dados sintéticos. Remova credenciais e informações privadas dos logs.
