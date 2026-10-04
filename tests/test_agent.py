from fastapi.testclient import TestClient
from agentx.main import app
client = TestClient(app)

def test_run_and_refuse():
    payload = client.post("/agent/run", json={"goal": 'why is the pod failing', "payload": {'events': ['Failed to pull image']}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["hypothesis"] == "image_pull"
    refused = client.post("/agent/run", json={"goal": 'kubectl delete pod api-0'}).json()
    assert refused["refused"] is True
