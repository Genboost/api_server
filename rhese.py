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
    Retourne ta réponse sous la forme d'un dictionnaire json, avec une clé texte_rhèse, qui contient en valeur le texte
        """

        # Appel au modèle de langage pour découper le texte
        response = llm.invoke(prompt)
        
        # Extraction de la réponse du modèle qui est sous forme de AIMessage
        rhese_output = response.content
        print(rhese_output)
        rhese_list = rhese_output["texte_rhèse"]
        
        # Transformation de la réponse en liste (si nécessaire)
        # rhese_list = rhese_output.split("\n")  # Suppose que les rhèses sont séparées par des sauts de ligne
        # return [rhese.strip() for rhese in rhese_list if rhese.strip()]
        return rhese_list
    
    except Exception as e:
        print(f"Erreur lors de l'appel au LLM : {e}")
        return []