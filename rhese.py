def decoupe_rhese(llm, input_text):
    """
    Découpe un texte en rhèses (unités de sens) en utilisant un LLM.
    
    Args:
        llm (ChatMistralAI): Instance du modèle de langage à utiliser.
        text (str): Le texte à découper.
    
    Returns:
        list: Une liste de rhèses (unités de sens).
    """
    try:
        # Construction du prompt pour le modèle de langage
        prompt = f"""
        Découpe le texte suivant en rhèses (unités de sens) :
        {input_text}
        Réponds uniquement avec les rhèses, séparées par des sauts de ligne.
        """

        # Appel au modèle de langage pour découper le texte
        response = llm.invoke(prompt)
        
        # Extraction de la réponse du modèle qui est sous forme de AIMessage
        rhese_output = response.content
        
        # Transformation de la réponse en liste (si nécessaire)
        rhese_list = rhese_output.split("\n")  # Suppose que les rhèses sont séparées par des sauts de ligne
        return [rhese.strip() for rhese in rhese_list if rhese.strip()]
    
    except Exception as e:
        print(f"Erreur lors de l'appel au LLM : {e}")
        return []