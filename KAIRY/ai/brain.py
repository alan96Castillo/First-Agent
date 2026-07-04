from tools.registry import listar
import ollama


def construir_prompt():

    herramientas = "\n".join(f"- {h}" for h in listar())

    return f"""
Eres KAIRY.

Tu única tarea es decidir si el usuario quiere usar una herramienta.

Herramientas disponibles:

{herramientas}

Si el usuario quiere usar una herramienta responde EXACTAMENTE:

Si necesitas una herramienta responde EXACTAMENTE así:

ACTION:abrir_web
url=https://gmail.com

Otro ejemplo:

ACTION:abrir_web
url=https://youtube.com

Si no necesitas herramientas responde:

RESPONSE:...
"""


def pensar(mensaje):

    respuesta = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "system",
                "content": construir_prompt()
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]
    )

    return respuesta["message"]["content"]