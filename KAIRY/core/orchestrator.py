from ai.brain import pensar
from tools.registry import ejecutar


class Orchestrator:

    def procesar(self, mensaje):

        respuesta = pensar(mensaje)

        if respuesta.startswith("ACTION:"):

            lineas = respuesta.splitlines()

            accion = lineas[0].replace("ACTION:", "").strip()

            parametros = {}

            for linea in lineas[1:]:

                if "=" in linea:

                    clave, valor = linea.split("=", 1)

                    parametros[clave.strip()] = valor.strip()

            return ejecutar(accion, **parametros)

        return respuesta