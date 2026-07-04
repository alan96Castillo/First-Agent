import subprocess
import webbrowser

from tools.registry import registrar


def abrir_calculadora():
    subprocess.Popen("calc.exe")
    return "Calculadora abierta."


def abrir_bloc():
    subprocess.Popen("notepad.exe")
    return "Bloc de notas abierto."


def abrir_google():
    webbrowser.open("https://google.com")
    return "Google abierto."

def abrir_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Youtube abierto."

def abrir_gmail():
    webbrowser.open("https://mail.google.com")
    return "Gmail abierto."

def abrir_facebook() :
    webbrowser.open("https://www.facebook.com")
    return "Facebook abierto."

registrar("abrir_calculadora", abrir_calculadora)
registrar("abrir_bloc", abrir_bloc)
registrar("abrir_google", abrir_google)
registrar("abrir_youtube", abrir_youtube)
registrar("abrir_gmail", abrir_gmail)
registrar("abrir_facebook", abrir_facebook)

print("System Tools cargado")