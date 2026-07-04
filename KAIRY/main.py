import tools.system_tools
import tools.browser_tools

from core.orchestrator import Orchestrator

kairy = Orchestrator()

while True:

    mensaje = input("Tú: ")

    if mensaje.lower() == "salir":
        break

    respuesta = kairy.procesar(mensaje)

    print("KAIRY:", respuesta)