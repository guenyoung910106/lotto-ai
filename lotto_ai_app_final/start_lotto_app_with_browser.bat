
@echo off
echo [1] Python 패키지 설치 중...
pip install -r requirements.txt

echo.
echo [2] Flask 서버 실행 중...
start "" http://localhost:5000
python app.py

pause
