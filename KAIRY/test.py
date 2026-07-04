from ollama import chat

respuesta = chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "user",
            "content": "Responde únicamente con: Hola Alan."
        }
    ]
)

print(respuesta.message.content)