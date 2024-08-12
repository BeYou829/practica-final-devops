import requests

def website_test():
    url = 'http://localhost:8000'
    response = requests.get(url)
    assert response.status_code == 200
    assert '<h1>Hola Mundo Este es Engel:)</h1>' in response.text