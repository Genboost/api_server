import os
from mistralai import Mistral
from flask import Flask, request, jsonify
from flask_cors import CORS
from rhese import decoupe_rhese

# Get the environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialisation du modèle de langage
llm = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
FLASK_PORT = os.getenv("FLASK_PORT", 5000)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return 'Index Page'

@app.route('/api/get_rhese', methods=['POST'])
def get_rhese ():
    # Récupérer le texte envoyé dans le corps de la requête
    data = request.get_json()
    # Vérifier si le texte est présent
    if 'text' not in data:
        return jsonify({'error': 'Aucun texte fourni'}), 400
    
    input_text = data['text']
    response_text = decoupe_rhese(llm, input_text)
    return response_text, 200, {'Content-Type': 'application/json'}


@app.route('/api/get_entites', methods=['POST'])
def get_entites():
    # Récupérer le texte envoyé dans le corps de la requête
    data = request.get_json()
    # Vérifier si le texte est présent
    if 'text' not in data:
        return jsonify({'error': 'Aucun texte fourni'}), 400
    
    input_text = data['text']
    #response_text = list_entites(llm, input_text)
    response_text = ""
    return response_text, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=True)
