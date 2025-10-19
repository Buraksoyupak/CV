import requests


def test_health_endpoint(base_url):
    url = f"{base_url}/health"
    resp = requests.get(url, timeout=10)
    assert resp.status_code in (200, 204)
