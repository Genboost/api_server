# <img src="images/Genboost-avatar-icon.png" alt="Icon" width="20" /> GenBoost api_server

Serveur API pour le moteur linguistique générant les enrichissements

<img src="images/genboost-avatar-zoom.png" alt="GenBoost Avatar" width="200" />

## Utilisation

Lancer le serveur avec la commande (port 5000 par défaut)

Lancement en local : `python ./run.py`

Lancement par Docker : `docker compose up -d --build`

## Lancement des tests unitaires

`pytest tests/``

## Requirements

- dotenv
- flask
- mistralai
- pytest
