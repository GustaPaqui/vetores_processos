import platform
import subprocess


def sistema_operacional():
    return platform.system()


def media_ping():

    so = sistema_operacional()

    if so == "Windows":
        comando = "ping -4 -n 10 www.google.com.br"

    else:
        comando = "ping -4 -c 10 www.google.com.br"

    resultado = subprocess.check_output(comando, shell=True).decode()

    linhas = resultado.split("\n")

    # Windows
    if so == "Windows":

        for linha in linhas:
            if "Média" in linha:
                partes = linha.split("=")
                media = partes[-1].strip()
                print(f"Média do ping: {media}")

    # Linux
    else:

        for linha in linhas:
            if "avg" in linha or "min/avg/max" in linha:

                partes = linha.split("=")[1].split("/")

                media = partes[1]
                print(f"Média do ping: {media} ms")


print(f"Sistema Operacional: {sistema_operacional()}")
media_ping()