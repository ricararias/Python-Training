# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
print("Digite a nota do aluno, a nota deve ser entre 0 e 10: ")

entrada = False
while entrada == False:
    nota = int(input("Nota: "))
    if nota < 0 or nota > 10:
        print("Valor inválido")
    else:
        entrada = True

print(f'A nota digitada foi {nota}')
'''

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
nome = input("Nome do usuário: ")

entrada = False
while entrada == False:
    senha = input("Senha: ")
    if senha == nome:
        print("A senha nao pode ser igual ao nome")
    else:
        entrada = True

print("Bem-vindo")
'''

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

'''
entrada = False
while entrada == False:
    nome = input("Nome: ")
    tamanho = len(nome)
    if tamanho < 3:
        print("O nome deve ter mais de 3 caracteres")
    else:
        entrada = True

while entrada == True:
    idade = int(input("Idade: "))
    if idade < 0 or idade > 150:
        print("Idade inválida!")
    else:
        entrada = False

while entrada == False:
    salario = float(input("Salário: "))
    if salario <= 0:
        print("Salário deve ser maior que zero!")
    else:
        entrada = True

while entrada == True:
    sexo = input("Sexo 'm' / 'f': ")
    if sexo != 'm' and sexo != 'f':
        print("Sexo só pode ser 'm' ou 'f'!")
    else:
        entrada = False

while entrada == False:
    EstadoCivil = input("Estado Civil 's', 'c', 'v', 'd': ")
    if EstadoCivil != 's' and EstadoCivil != 'c' and EstadoCivil != 'v' and EstadoCivil != 'd':
        print("Estado Civil inválido!")
    else:
        entrada = True

print(f'\nNome: {nome}')
print(f'Idade: {idade}')
print(f'Salario: R$ {salario:,.2f}')
print(f'Sexo: {sexo}')
print(f'Estado Civil: {EstadoCivil}\n')
'''

#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual 
#de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento 
#de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população 
#do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
import math

paisA = 80000
paisB = 200000
crescA = 3
crescB = 1.5
anos = 0

while paisA <= paisB:
    paisA += (paisA * crescA) / 100
    paisB += (paisB * crescB) / 100
    anos += 1

print(f'População país A: {math.floor(paisA)}')
print(f'População país B: {math.floor(paisB)}')
print(f'Anos: {anos}')
'''

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
#crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
import math

anos = 0

paisA = int(input("Digite a quantidade da população do país A: "))
crescA = float(input("Digite a taxa de crescimento do país A: "))
paisB = int(input("Digite a quantidade da população do país B: "))
crescB = float(input("Digite a taxa de crescimento do país B: "))
print("\n")

if paisB > paisA:
    while paisA <= paisB:
        paisA += (paisA * crescA) / 100
        paisB += (paisB * crescB) / 100
        anos += 1
    if paisA > paisB:
        print(f'O país A ficou superior ao país B após {anos} anos')
        print(f'População país A: {math.floor(paisA)}')
        print(f'População país B: {math.floor(paisB)}')
    else:
        print(f'O país A ficou igual ao país  após {anos} anos')
        print(f'População país A: {math.floor(paisA)}')
        print(f'População país B: {math.floor(paisB)}')

else:
    while paisB <= paisA:
        paisA += (paisA * crescA) / 100
        paisB += (paisB * crescB) / 100
        anos += 1
    if paisA < paisB:
        print(f'O país B ficou superior ao país A após {anos} anos')
        print(f'População país A: {math.floor(paisA)}')
        print(f'População país B: {math.floor(paisB)}')
    else:
        print(f'O país B ficou igual ao país A após {anos} anos')
        print(f'População país A: {math.floor(paisA)}')
        print(f'População país B: {math.floor(paisB)}')

'''

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
#Depois modifique o programa para que ele mostre os números um ao lado do outro.
'''
numeros = []
for i in range(20):
    numeros.append(i + 1)
print(numeros)

for i in range(20):
    print(numeros[i])
'''


#Faça um programa que leia 5 números e informe o maior número.
'''
lista = []
print("Digite 5 numeros\n")
for i in range(5):
    elemento = float(input(f'Digite o numero {i + 1}: '))
    lista.append (elemento)

print(f'O maior numero da lista é {max(lista)}')
'''

#Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
numeros = []
soma = 0
media = 0

print("Digite 5 numeros\n")
for i in range(5):
    elemento = int(input(f'Digite o numero {i+1}: '))
    numeros.append(elemento)

for i in range(len(numeros)):
    soma += numeros[i]

media = soma / (len(numeros))

print(f'A soma dos números é: {soma}')
print(f'A média dos números é: {media}')
'''

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

'''
numeros = []
for i in range(50):
    if ((i+1) % 2) != 0:
        numeros.append(i+1) 

print(numeros)
'''

#Faça um programa que receba dois números inteiros e gere os números inteiros que estão 
#no intervalo compreendido por eles.
'''
numeros = []
print("Digite dois numeros inteiros")
num1 = int(input("Digite o numero inteiro 1: "))
num2 = int(input("Digite o numero inteiro 2: "))

for i in range(num2):
    if i > num1:
        numeros.append(i)

print(numeros)
'''

#Altere o programa anterior para mostrar no final a soma dos números.
'''
numeros = []
print("Digite dois numeros inteiros")
num1 = int(input("Digite o numero inteiro 1: "))
num2 = int(input("Digite o numero inteiro 2: "))

for i in range(num2):
    if i > num1:
        numeros.append(i)

print(numeros)

soma = 0
for i in range(len(numeros)):
    soma += numeros[i]

print(f'Soma dos numeros: {soma}')
'''

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
#entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
#A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:
#5 X 1 = 5
#5 X 2 = 10
#...
#5 X 10 = 50
'''
entrada = False
while entrada == False:
    numero = int(input("Digite um numero de 1 a 10 para calculo da tabuada: "))
    if numero < 1 or numero > 10:
        print("O numero deve ser de 1 ao 10!")
    else:
        entrada = True

for i in range(10):
    print(f'{numero} x {i+1} = {numero * (i+1)}')
''' 

#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número 
#elevado ao segundo número. Não utilize a função de potência da linguagem.

'''
print("Digite dois numeros, base e expoente")
base = int(input("Base: "))
expoente = int(input("Expoente: "))
potencia = 1

for i in range(expoente):
    potencia *= base

print(f'Base {base} com expoente {expoente} = {potencia}')
'''

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares 
#e a quantidade de números impares.
'''
numero = []
par = 0
impar = 0
for i in range(10):
    valor = int(input(f'{i+1} digite um numero: '))
    numero.append(valor)

for i in range(10):
    if numero[i] % 2 == 0:
        par += 1
    else:
        impar +=1

print(f'Pares: {par}')
print(f'Impares: {impar}')
'''

#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa 
#capaz de gerar a série até o n−ésimo termo.

'''
enesimo = int(input("Digite o enesimo termo: "))
fibonacci = [1,1]
x = 1
y = 1

for i in range(enesimo):
    y = x + y
    fibonacci.append(y)
    x = fibonacci[i + 1]

print(fibonacci)

'''

# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa que gere a série até que o valor seja maior que 500.
'''
fibonacci = [1,1]
x = 1
y = 1
condicao = True
i = 0

while condicao == True:
    y = x + y
    fibonacci.append(y)
    x = fibonacci[i + 1]
    i = i + 1
    if y > 500:
        condicao = False

print(fibonacci)                      
'''

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
fatorial = int(input('Numero para calculo de fatorial: '))
anterior = fatorial - 1

while anterior != 1:
    fatorial *= anterior
    anterior = anterior - 1

print(fatorial)
'''    

#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''
qtde = int(input("Quantos numeros no conjunto? "))
numeros = []
soma = 0

for i in range(qtde):
    valor = int(input(f'{i+1} Digite um numero:'))
    numeros.append(valor)
    soma += numeros[i]

print(f'O menor numero do conjunto{min(numeros)}')
print(f'O maior numero do conjunto{max(numeros)}')
print(f'A soma dos numeros do conjunto{soma}')
'''

#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
qtde = int(input("Quantos numeros no conjunto? "))
numeros = []
soma = 0

for i in range(qtde):
    while True:
        valor = int(input(f'{i+1} Digite um numero no intervalo 0 - 1000: '))
        if valor <= 1000:
            numeros.append(valor)
            soma += numeros[i]
            break 
        else:
            print("O valor não pode ser superior a 1000")
            
print(f'O menor numero do conjunto: {min(numeros)}')
print(f'O maior numero do conjunto: {max(numeros)}')
print(f'A soma dos numeros do conjunto: {soma}')
'''

#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
#e limitando o fatorial a números inteiros positivos e menores que 16.
'''
print("\nCalculo de fatorial para numeros inteiros, positivos e menores que 16")
continua = True
while continua == True:
    entrada = input("Deseja calcular fatorial de um numero? (s / n): ")
    if entrada == 's':
        while True:
            fatorial = int(input('Numero para calculo de fatorial: '))
            escolha = fatorial
            if fatorial == 0 or fatorial == 1:
                fatorial = 1
                print(f'fatorial de {escolha}: {fatorial}')
                break
            elif fatorial > 1 and fatorial <= 16:
                anterior = fatorial - 1
                while anterior != 1:
                    fatorial *= anterior
                    anterior = anterior - 1
                print(f'fatorial de {escolha}: {fatorial}')
                break
            else:
                print("O numero de ser inteiro, positivo e menos que 16")
    else:
        print("Obrigado!")
        continua = False
'''

#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
#Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''
numero = int(input("Digite um numero: "))
if numero % 2 != 0:
    if numero % 3 != 0:
        if numero % 5 != 0:
            if numero % 7 != 0:
                if numero % 11 != 0:
                    if numero % 13 != 0:
                        print("O numero é primo")
else:
    print("O numero NAO é primo")
'''
    
#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
#por quais número ele é divisível.
'''
numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print("O numero é par, multiplo de 2")
elif numero % 3 == 0:
    print("O numero é multiplo de 3")
elif numero % 5 == 0:
    print("O numero é multiplo de 5")
elif numero % 7 == 0:
    print("O numero é multiplo de 7")
elif numero % 11 == 0:
    print("O numero é multiplo de 11")
elif numero % 13 != 0:
    print("O numero é primo")
else:
    print("O numero NAO é primo")
'''

#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
#pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
#encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes 
#(divisões) executados.





#Faça um programa que calcule o mostre a média aritmética de N notas.

print("Calculo de média de N notas")

numero = int(input("Quantas notas serão calculadas: "))
soma = 0
notas = []

for i in range(numero):
    valor = int(input(f"Digite a nota {i+1}: "))
    notas.append(valor)
    soma += notas[i]

media = soma / numero

print(f'Média das {numero} notas informadas: {media:,.2f}')


