from responseLLM import responseLLM

def list_entites(llm, input_text, model="mistral-large-latest"):
    try:
        prompt = f"""tu es un spécialiste des dyslexique depuis 20 ans. 
            Voici un texte : 
            {input_text}
            Réécris moi le texte selon la manière suivante : les entités nommés seront entre crochets,
            et tu fournis l'explication ensuite. L'ensemble respectera les contraintes markdown
            [entité nommé](explication),les explications seront là pour aider les dys concernant les entités
            nommés qui sont compliqués à comprendre pour un dysléxique.
            Retourne ta réponse sous la forme d'un dictionnaire json avec comme clé response"""

        rhese_output = responseLLM(llm, model, prompt)
        
        return rhese_output

    except Exception as e:
        print(f"Erreur lors de l'appel au LLM : {e}")