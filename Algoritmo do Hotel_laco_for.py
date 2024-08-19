# Pergunta ao usuário em qual andar ele está
andar_usuario = input("Em que andar você está? ")

# Mensagem informativa
print("Aqui estão os andares do hotel (exceto o 13):")

# Laço para imprimir os andares, exceto o 13
for i in range(20, 0, -1):
    if i != 13:
        print(i)

