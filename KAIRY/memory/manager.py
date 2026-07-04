import json
from pathlib import Path

RUTA = Path(__file__).parent / "data.json"


def cargar():

    with open(RUTA, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar(datos):

    with open(RUTA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def recordar(clave, valor):

    datos = cargar()

    datos[clave] = valor

    guardar(datos)


def obtener(clave):

    datos = cargar()

    return datos.get(clave)