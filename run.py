import os
from langchain_mistralai.chat_models import ChatMistralAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from rhese import decoupe_rhese
from entites import list_entites

# Get the environment variables
from dotenv import load_dotenv
load_dotenv()

# Activation de Langfuse pour le suivi des appels
DEBUG_LANGFUSE = os.getenv("DEBUG_LANGFUSE", "False").lower() == "true"
LANGFUSE_URL = os.getenv("LANGFUSE_URL", False)
if DEBUG_LANGFUSE and LANGFUSE_URL:
    import uuid
    from langfuse.callback import CallbackHandler

    try:
        session_id = str(uuid.uuid4())
        langfuse_handler = CallbackHandler(
            secret_key=os.getenv("LANGFUSE_SK"),
            public_key=os.getenv("LANGFUSE_PK"),
            host=os.getenv("LANG_FUSE_URL"),
            session_id=session_id
        )
        langfuse_handler.auth_check()
        config = {"callbacks": [langfuse_handler]}
    except:
        DEBUG_LANGFUSE = False
        config = {}
else:
    config = {}

# Initialisation du modèle de langage
#llm = ChatMistralAI(model="mistral-large-latest", temperature=0, max_retries=2,
#                    api_key=os.getenv("MISTRAL_API_KEY"), config=config)
llm = ChatMistralAI(model="mistral-large-latest", temperature=0, max_retries=2,
                    api_key=os.getenv("MISTRAL_API_KEY"))

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
    return jsonify({'response': response_text}), 200


@app.route('/api/get_entites', methods=['POST'])
def get_entites():
    # Récupérer le texte envoyé dans le corps de la requête
    data = request.get_json()
    # Vérifier si le texte est présent
    if 'text' not in data:
        return jsonify({'error': 'Aucun texte fourni'}), 400
    
    input_text = data['text']
    response_text = list_entites(llm, input_text)
    return jsonify({'response': response_text}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
