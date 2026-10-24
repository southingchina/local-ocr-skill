# Local OCR Skill

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Français](README.fr.md) | [Deutsch](README.de.md) | [Português (Brasil)](README.pt-BR.md)

이미지의 텍스트를 추출하는 로컬 Umi-OCR HTTP 클라이언트이자 명시적으로 호출하는 Codex Skill입니다. 문단 또는 코드 레이아웃과 이미지 크기를 선택하고 텍스트나 구조화된 JSON을 출력할 수 있습니다. 클라이언트는 루프백 주소만 허용합니다. Python 코드는 표준 라이브러리만 사용하며 Umi-OCR과 언어 모델은 별도로 설치하고 HTTP API를 켜야 합니다.

## 필요 환경

Python 3.10+; Umi-OCR HTTP API

## 설정 및 진입점

`UMI_OCR_EXE`, `--umi-exe`, `--endpoint`, `--no-start`, `--layout`, `--max-side`, `--format`, `--output`

## 설치 및 사용

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


## 공개 범위와 제한

기본 API는 http://127.0.0.1:1224/api/ocr입니다. Windows의 숨김 실행에는 UMI_OCR_EXE 또는 --umi-exe를 지정하고, 이미 실행 중인 엔진에는 --no-start를 사용하세요. --endpoint로 원격 서버를 지정할 수 없습니다. 정확도, 표와 읽기 순서는 엔진에 의존하므로 확인이 필요합니다. 엔진, 모델, 개인 이미지나 클라우드 대체 경로는 포함하지 않습니다. 스캔 PDF는 먼저 이미지로 변환하세요.

## 검증 기록

2026-10-24 · Python: 4 ✓

## 라이선스 및 출처

[MIT](LICENSE)

프로젝트 문서의 언어별 버전입니다. 앱 화면, CLI 출력과 실행 파일은 현재 구현을 따릅니다.

[중국어 상세 참고 문서](README.zh-CN.md) · [언어 문서 유지 관리 정책](docs/LOCALIZATION.md)

[Issues](https://github.com/southingchina/local-ocr-skill/issues) — 재현 가능한 문제는 합성 데이터로 보고하고 로그의 자격 증명과 개인 정보를 제거하세요.
