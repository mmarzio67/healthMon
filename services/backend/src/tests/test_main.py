from starlette.testclient import TestClient

from main import app

## test_app is a fixture therefor pytest looks for fixture called test_app
def test_welcome(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == "Hello, World from FastAPI backend!"
