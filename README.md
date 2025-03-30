# <img src="images/Genboost-avatar-icon.png" alt="Icon" width="20" /> GenBoost api_server

Serveur API pour le moteur linguistique générant les enrichissements

<img src="images/Genboost-avatar-zoom.png" alt="GenBoost Avatar" width="200" />

## Utilisation

Lancer le serveur avec la commande (port 5000 par défaut)

Lancement en local : `python ./run.py`

Lancement par Docker : `docker compose up -d --build`

## Requirements

- dotenv
- flask
- flask-cors
- mistralai
- pytest

Pour les installer : `pip install -r requirements.txt`

## Lancement des tests unitaires

`pytest tests/`


## Mode d'emploi pour un hébergement sur Scaleway

Scaleway propose un système d'hébergement de containers qui se prête particulièrement bien à l'hébergement de ce serveur de démo.

ATTENTION : l'explication suivante correspond à un usage ponctuel pour une démo, ce n'est pas une installation compatible pour un usage en production (pas de sécurité entre le front et le back, utilisation de Flask pour le serveur d'API et en mode debug, etc.)

1. Créer un compte Scaleway et le configurer
    1. Créer un compte sur [Scaleway](https://console.scaleway.com)
    1. Créer une "police" qui autorise l'exécution des containers. La nommer par exemple "Compute containers" et lui attribuer les droits suivants
        - Sur les projets
            - `ContainerRegistryFullAccess` : pour autoriser à créer/modifier des images de type Docker
            - `ContainersFullAccess` : pour lancer et arrêter des containers
        - Sur l'organisation
            - `ProjectReadOnly` : pour permettre la connexion initiale de l'application par Docker
    1. Créer un utilisateur d'application
        - Dans la partie IAM de la console, créer un utilisateur de type "applications", en le nommant par exemple "applications-genboost-apiserver" et lui affecter la "police" créée précédemment
    1. Créer une clé d'API pour cet utilisateur et conserver les deux informations générées que sont `Access Key` et `Secret Key`
    1. Récupérer le `Project ID` sur la console Scaleway
        - Celui-ci est disponible sur la page "Dashboard" à côté du nom du projet
    1. Créer un `namespace` dans le `Container Registry`
        - Il s'agit de l'endroit où l'on va charger l'image Docker du serveur qui sera exécuté
        - Noter le nom de ce `namespace`
    1. Créer un `namespace` dans les `Containers` de la partie `Serverless`, pour l'instant on n'ajoute pas de le containeur. Récupérer le `endpoint du Registry`
1. Installer et configurer Docker
    1. Installer Docker sur votre ordinateur, cloner ce repository
    1. Configurer Docker pour lui donner accès à votre repository sur Scaleway
        - Lancer la commande `docker login rg.fr-par.scw.cloud` (changer si nécessaire l'URL en fonction de la région souhaitée pour l'exécution, il s'agit de celle sélectionnée dans la création du namespace du container)
        - Renseigner `Access Key`, `Secret Key`, `Project ID`
1. Créer un compte Mistral et configurer le serveur
    1. Créer un compte Mistral sur [la console](https://console.mistral.ai) et générer une clef API
    1. Cloner ce repository et créer un fichier `.env` en dupliquant le fichier `example.env` puis modifier la clef API pour utiliser celle créée au point précédent
1. Construire l'image Docker et la charger sur Scaleway
    - Construire l'image avec la commande suivante en remplaçant les items entre < et > : `docker build --platform linux/amd64 -t <endpoint du Registry>/api_server-web:v1 .`
    - Charger l'image sur Scaleway avec la commande suivante : `docker push <endpoint du Registry>/api_server-web:v1`
1. Lancer le serveur
    - Aller sur le conteneur créée précédemment dans console de Scaleway et cliquer sur "Déployer le conteneur"
    - Sélectionner :
        - Le registre précédemment créé
        - L'image `api_server-web` (qui est normalement la seule disponible) et la version `v1`
        - Indiquer le port 5000
    - Pour les ressources il est possible de mettre le minimum : 100 mVCPU et 128 MB (ou 256 MB idéalement)
    - Pour l'autoscaling positionner le maximum à 1 pour limiter les frais d'hébergement
    - A la fin de la configuration le serveur va démarrer, il suffit alors d'attendre que le déploiement soit réussi et de copier le `endpoint du conteneur` pour configurer cette URL sur l'application web
