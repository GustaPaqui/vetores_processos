vetor = []
soma = 0


for i in range(30):
    valor = float(input(f"Digite o {i+1}º valor: "))
    vetor.append(valor)
    soma += valor


media = soma / 30


acima_media = 0

print("\nPosições abaixo da média:")

for i in range(30):

    if vetor[i] > media:
        acima_media += 1

    if vetor[i] < media:
        print(f"Posição {i}")


print(f"\nMédia do grupo: {media}")
print(f"Quantidade acima da média: {acima_media}")