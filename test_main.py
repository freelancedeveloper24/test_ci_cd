from fastapi.testclient import TestClient
from main import app  # replace 'main' with your filename if different
import os

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_say_hello(monkeypatch):
    monkeypatch.setenv("My_key", "CI_CD")
    response = client.get("/hello/")
    assert response.status_code == 200
    assert response.json() == {"message": "test env CI_CD "}
