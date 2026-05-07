import platform
import subprocess


def os():

    return platform.system()


def processo_filho(opcao, parametro=None):

    sistema = os()

    
    if opcao == 1:

        if sistema == "Windows":
            comando = "TASKLIST /FO TABLE"

        else:
            comando = "ps -ef"

    
    elif opcao == 2:

        if sistema == "Windows":
            comando = f"TASKKILL /PID {parametro}"

        else:
            comando = f"kill -9 {parametro}"

    
    elif opcao == 3:

        if sistema == "Windows":
            comando = f"TASKKILL /IM {parametro}"

        else:
            comando = f"pkill -f {parametro}"

    else:
        return

    subprocess.run(comando, shell=True)

# MAIN
while True:

    print("\n1 - Listar processos")
    print("2 - Matar processo por PID")
    print("3 - Matar processo por nome")
    print("9 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        processo_filho(1)

    elif opcao == 2:

        pid = input("Digite o PID: ")
        processo_filho(2, pid)

    elif opcao == 3:

        nome = input("Digite o nome do processo: ")
        processo_filho(3, nome)

    elif opcao == 9:

        print("Encerrando aplicação...")
        break

    else:

        print("Opção inválida!")