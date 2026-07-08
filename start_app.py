import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def start_http_server():
    subprocess.Popen(
        [sys.executable, "-m", "http.server", "8000"],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(1)


def start_streamlit():
    subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "ui/app.py", "--server.port", "8501"],
        cwd=str(ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    time.sleep(2)


if __name__ == "__main__":
    start_http_server()
    start_streamlit()
    print("Started local sample page server on http://127.0.0.1:8000")
    print("Started Streamlit UI on http://127.0.0.1:8501")
