import pytest
from run import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_rhese(client):
    input_text = "Le soleil brille aujourd'hui. Les oiseaux chantent dans les arbres. C'est une belle journée."
    # Corps de la requête
    data = {"text": input_text}
    
    # Envoyer une requête POST à l'API
    response = client.post('/api/get_rhese', json=data)
    
    # Vérifier que le code de statut est 200
    assert response.status_code == 200
    
    # Récupérer la réponse JSON
    response_json = response.get_json()
    
    # Vérifier que la réponse contient les rhèses attendues
    expected_rheses = [
        "Le soleil brille aujourd'hui.",
        "Les oiseaux chantent dans les arbres.",
        "C'est une belle journée."
    ]
    assert response_json['response'] == expected_rheses