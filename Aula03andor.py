idade = int(input("Idade: "))
dinheiro = int(input("Quanto de dinheiro vc tem: "))
carteira = input("Você tem carteira de motorista? (s/n)")

if (idade >= 18 or dinheiro >= 50) or carteira == "s":
    print("Você pode alugar o carro.")
else: 
    print("Você não pode alugar o carro.")