# movie-API-with-FastAPI

### 1. Create, activate virtual environment and download packages
  `python3 -m venv venv` <br>
  `source venv/bin/activate` <br>
  `pip install fastapi` <br>
  `pip install uvicorn`

### 2. Ways to execute
  `uvicorn main:app` <br>
  `uvicorn main:app --reload --port 5000` <br>
  `uvicorn main:app --reload --port 5000 --host 0.0.0.0`
