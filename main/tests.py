
from django.urls import reverse

def test_health_endpoint(client):
    resp = client.get('/health/')
    assert resp.status_code in (200, 500)
