#tipos de concatenaçao
#concatenaçao com sinal +
#num = int(input("digite um numero inteiro: "))

#nao possivel concatenar numero inteiro usando esse metodo, a que
#converta o numero inteiro em uma string
#print(("ola, "+ str(num)) + ". Seja bem vindo!")

#concatenaçao com a (,)

#print(" o numero digitado e: ",num)

#concatenaçao com fstring (f)

#print(f"o numero digitado e: {num} usando a concatenaçao 'f'")

#div = num / 3
#usando format para formataçao numerica 
#limitando a quantidade de casas decimais 
#print(f"o resultado da divisao e: {div:.2f}")


print("----------------------------")
print("        ATIVIDADE           ")
print("----------------------------")

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
tel = float(input("Digite seu telefone: "))
valor_gasosa = float(input("Digite o valo da gasolina: "))
valor_alc = float(input("Digite o valor do alcool: "))
capacidade_tanq = 55
distn = int(input("Digite a distancia percorrida no dia: "))
kml = 14

print("Nome: ",nome)
print("E-mail: ",email)
print("Telefone: ",tel)

total_per = (distn*2)(*5)*4
vlrmensal = (total_per/kml)*valor_gasosa
vlrmenalc = (total_per/kml)*valor_alc
mddkms = total_per/4


print(f"O valor mensal gasto na gasolina vai ser de: {vlrmensal:.2f}")
print(f"O valor mensaç gasto no alcool vai ser de:{vlrmenalc:.2f}")
print("O toltal de kilometros percorrido vai ser de: ",total_per, "KM")
print("A media de kilometros semanalmete vai ser de: ",mddkms, "KMs")












