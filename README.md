# api_server

Serveur API pour le moteur linguistique générant les enrichissement

## Utilisation

Lancer le serveur avec la commande

Lancement en local (port 5000 par défaut) : `python ./run.py`

Lancement par Docker (port 5001) : `docker compose up -d --build`

## Lancement des tests unitaires

`pytest tests/``

## Requirements

- dotenv
- flask
- mistralai
- pytest
