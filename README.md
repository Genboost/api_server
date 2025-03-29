# api_server

Serveur API pour le moteur linguistique générant les enrichissement

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
