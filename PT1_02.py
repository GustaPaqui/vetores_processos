vetor = []


for i in range(100):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)


maior = max(vetor)
menor = min(vetor)
media = sum(vetor) / len(vetor)


print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Média dos valores: {media}")