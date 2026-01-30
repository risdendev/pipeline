# Run the FastAPI app with reload, excluding .venv from the file watcher
uvicorn app.main:app --reload --reload-exclude .venv --host 0.0.0.0 --port 8000
