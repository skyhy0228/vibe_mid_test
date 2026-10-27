# 강의실 예약 시스템

바이브코딩 실기 시험 과제입니다. 과제 설명은 [PROBLEM.md](PROBLEM.md)에 있습니다.

## 구성

| 파일 | 역할 |
|---|---|
| `solution.py` | 예약 규칙이 담긴 `RoomBooking` 클래스 (`book`, `cancel`, `get_schedule`) |
| `index.html` | 예약 웹페이지. 브라우저에서 [Pyodide](https://pyodide.org)로 `solution.py`를 그대로 불러와 사용 |
| `check.py` | 샘플 테스트 5개 |

웹페이지에는 예약 규칙이 따로 없습니다. 입력값을 `solution.py`의 `RoomBooking`에 넘기고 결과만 보여줍니다.
예약 정보는 페이지가 열려 있는 동안만 유지되고, 새로고침하면 초기화됩니다.

## 실행

```bash
# 샘플 테스트
python check.py

# 웹페이지 로컬 실행 (file:// 로 열면 solution.py 를 불러올 수 없음)
python -m http.server 8000
# → http://localhost:8000
```

## 배포

GitHub Pages (`main` 브랜치 루트)로 배포합니다. `solution.py`나 `index.html`을 고친 뒤 push하면 1~2분 뒤 반영됩니다.
