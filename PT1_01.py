vetor = []

soma_impares = 0
soma_intervalo = 0
contador_intervalo = 0

# Entrada de dados
for i in range(50):

    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

# Processamento
for num in vetor:

    # Soma dos ímpares
    if num % 2 != 0:
        soma_impares += num

    # Valores entre 10 e 200
    if num >= 10 and num <= 200:
        soma_intervalo += num
        contador_intervalo += 1

# Média
if contador_intervalo > 0:
    media = soma_intervalo / contador_intervalo
else:
    media = 0

# Saída
print("\nRESULTADOS")
print(f"Média entre 10 e 200: {media}")
print(f"Soma dos números ímpares: {soma_impares}")