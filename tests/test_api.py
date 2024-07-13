import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_export_data_csv():
    response = client.post("/export-data/", json=[
        {"value": 10.5, "label": "A"},
        {"value": 20.3, "label": "B"},
        {"value": 15.8, "label": "C"}
    ], params={"format": "csv"})
    
    assert response.status_code == 200
    assert "data" in response.json()

def test_export_data_json():
    response = client.post("/export-data/", json=[
        {"value": 10.5, "label": "A"},
        {"value": 20.3, "label": "B"},
        {"value": 15.8, "label": "C"}
    ], params={"format": "json"})
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_export_data_invalid_format():
    response = client.post("/export-data/", json=[
        {"value": 10.5, "label": "A"},
        {"value": 20.3, "label": "B"},
        {"value": 15.8, "label": "C"}
    ], params={"format": "invalid"})
    
    assert response.status_code == 400
    assert "detail" in response.json()

def test_calculate_statistics():
    response = client.post("/statistics/", json=[
        {"value": 10.5, "label": "A"},
        {"value": 20.3, "label": "B"},
        {"value": 15.8, "label": "C"}
    ])
    
    assert response.status_code == 200
    stats = response.json()
    assert "mean" in stats
    assert "median" in stats
    assert "std_dev" in stats
    assert "percentiles" in stats

def test_websocket_analysis():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_json({"value": 10})
        response = websocket.receive_json()
        assert response["mean"] == 10
        assert response["median"] == 10
        assert response["std_dev"] == 0
        assert response["percentiles"]["25th"] == 10
        assert response["percentiles"]["50th"] == 10
        assert response["percentiles"]["75th"] == 10
        
        websocket.send_json({"value": 20})
        response = websocket.receive_json()
        assert response["mean"] == 15
        assert response["median"] == 15
        assert response["std_dev"] == pytest.approx(7.071, rel=1e-3)
        assert response["percentiles"]["25th"] == pytest.approx(12.5, rel=1e-3)
        assert response["percentiles"]["50th"] == 15
        assert response["percentiles"]["75th"] == 20
