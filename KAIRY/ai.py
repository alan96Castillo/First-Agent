from ollama import chat

MODEL = "qwen3:8b"

def preguntar(mensaje):

    respuesta = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": mensaje
            }
        ]
    )

    return respuesta.message.content