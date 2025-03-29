import json
from flask import jsonify


def decoupe_rhese(llm, input_text, model="mistral-large-latest"):
    """
    Découpe un texte en rhèses (unités de sens) en utilisant un LLM.
    
    Args:
        llm (Mistral): Instance du modèle de langage à utiliser.
        text (str): Le texte à découper.
        model (str): Le modèle de langage à utiliser (par défaut : "mistral-large-latest").
    
    Returns:
        response: un json contenant une variable "response" qui contient la liste des rhèses.
    """
    try:
        # Construction du prompt pour le modèle de langage
        prompt = f"""
        Tu es un expert linguistique, tu vas découper le texte suivant en rhèse. L'objectif est de limiter l'effort cognitif de lecture pour un collégien dyslexique. Renvoie le texte rhésé sous forme de liste. Ne modifie pas le texte : Ne change pas les mots ou la structure des phrases.
    Rhèses courtes : Découpe le texte en segments très courts
    Respecte la ponctuation : Conserve les signes de ponctuation pour maintenir le sens des phrases.
        Voici le texte à découper :
        [{input_text}]
        Merci de suivre ces consignes pour aider l'élève à mieux comprendre le texte.
    Retourne ta réponse sous la forme d'un dictionnaire json, avec une clé response, qui contient en valeur le texte
        """

        # Appel au modèle de langage pour découper le texte
        response = llm.chat.complete(
            model= model,
            messages = [
                {
                    "role": "user",
                    "content": prompt
                },
            ],
            response_format = {
                "type": "json_object",
            }
        )
        # Extraction de la réponse du modèle qui est sous forme de AIMessage
        rhese_output = response.choices[0].message.content
        rhese_list = json.loads(rhese_output)

        return rhese_list
    
    except Exception as e:
        print(f"Erreur lors de l'appel au LLM : {e}")
        return []