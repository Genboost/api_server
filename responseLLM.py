def responseLLM(llm, model, prompt):
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
    return response.choices[0].message.content