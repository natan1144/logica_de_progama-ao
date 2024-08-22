nome = "natan"
idade = 18

print(nome)
print(f"O nome é {nome}")

peso = input("Digite seu peso: ")

num1 = input("Digite o primeiro numero: ")
num1 = int(num1)

num2 = int(input("Digite o segundo numero: "))

#operadores matematicos
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2
divi_inteira = num1 // num2
expo = num1 ** num2 
modulo = num1 % num2 #O resto da divisaoo


# FIXME: Operadores comparativos
print("Operadores comparativos")
print(num1 > num2) # maior que
print(num1 < num2) # menor que 
print(num1 == num2) # igualdade
print(num1 != num2) # diferente 
print(num1 <= 100) # menor ou igual

print(num1 <= 100 and num2 <=100 or (num1 + num2 > 100))

 # FIXME: Operadores matematicos 
print("Operadores matematicos no print")
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#Atribuicoes de valores 
num1 += 1
#num1 -= 1
#num1 *= 1 
#num1 /= 1

print(f"soma: {soma}")
print(f"subtraçao: {sub}")
print(f"mutiplicaçao: {mult}")
print(f"divisao: {divi}")
print(f"divisao inteira: {divi_inteira}")
print(f"divisao formatada: {divi:.2f}")
print(f"exponenciaçao: {expo}")
print(f"resto da divisao: {modulo}")
print()
print(f"O numero digitado +1 e: {num1}")






