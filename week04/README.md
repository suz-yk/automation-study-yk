# Python 4주차 과제 - 가상환경 및 환경설정 분리

프로젝트별 독립된 파이썬 실행 환경을 구성하고, 보안 및 설정값을 외부(`.env`)에서 관리하도록 설계.

---

## 1. 실행 환경 준비 방법 (가상환경 생성)

프로젝트 최상위 루트 디렉토리에서 가상환경을 생성하고 활성화.

### Windows (Bash / PowerShell)
```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
source .venv/Scripts/activate  # Git Bash
# 또는
.venv\Scripts\activate          # PowerShell / CMD