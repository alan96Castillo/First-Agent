import webbrowser

from tools.registry import registrar


def abrir_web(url):

    webbrowser.open(url)

    return f"Abriendo {url}"


registrar("abrir_web", abrir_web)