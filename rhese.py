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
        Découpe le texte suivant en rhèses (unités de sens) :
        {input_text}
        Réponds uniquement avec la liste des rhèses dans la variable "response" au sein d'un JSON.
        """

        # Appel au modèle de langage pour découper le texte
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
        response = llm.chat.complete(model=model, messages=messages, response_format={"type": "json_object"})
        return (response.choices[0].message.content)
    
    except Exception as e:
        print(f"Erreur lors de l'appel au LLM : {e}")
        return []