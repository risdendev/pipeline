from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_rejects_non_csv():
    response = client.post("upload", files={"file":("data.txt","text/plain")})
    assert response.status_code == 400

