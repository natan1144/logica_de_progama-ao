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

#informando nome, email e telefone
nome =input('\nDigite seu nome completo: ')
email =input('Digite o seu email: ')
fone =int(input ('Digite o seu telefone: '))

#informando km, valor da gasolina e valor do alcool 1ª semana
km1se= float(input('\nInforme quantos Km você percorreu na 1º semana: '))
gaso1 =float(input('Digite o valor do litro de gasolina na 1º semana : '))
alcool1 = float(input('Digite o valor do litro do álcool na 1º semana: '))
#variaveis de gasto 1º semana
gastogasos1 =gaso1*(km1se/14)
gastoalcos1 = alcool1*(km1se/12)

#informando km, valor da gasolina e valor do alcool 2ª semana
km2se= float(input('\nInforme quantos Km você percorreu na 2º semana: '))
gaso2 =float(input('Digite o valor do litro de gasolina na 2º semana : '))
alcool2= float(input('Digite o valor do litro do álcool na 2º semana: '))
#variaveis de gasto 2º semana
gastogasos2 =gaso2*(km2se/14)
gastoalcos2 = alcool2*(km2se/12)

#informando km, valor da gasolina e valor do alcool 3ª semana
km3se= float(input('\nInforme quantos Km você percorreu na 3º semana: '))
gaso3 =float(input('Digite o valor do litro de gasolina na 3º semana : '))
alcool3 = float(input('Digite o valor do litro do álcool na 3º semana: '))
#variaveis de gasto 3º semana
gastogasos3 =gaso3*(km3se/14)
gastoalcos3 = alcool3*(km3se/12)








