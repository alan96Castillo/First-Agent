TOOLS = {}

def registrar(nombre, funcion):
    TOOLS[nombre] = funcion


def obtener(nombre):
    return TOOLS.get(nombre)


def listar():
    return list(TOOLS.keys())


def ejecutar(nombre, **kwargs):
    herramienta = obtener(nombre)

    if herramienta:
        return herramienta()

    return f"No existe la herramienta '{nombre}'."