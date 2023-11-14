#Faça um Programa que peça dois números e imprima o maior deles.
'''
num1= input("Digite um numero: ")
num2= input("Digite mais um numero: ")

if num1 > num2:
    print("O maior numero é: " + str(num1))
else:
    print("O maior numero é: " + str(num2))
'''

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''
numero= float(input("Digite um numero: "))

if numero > 0:
    print("O numero " + str(numero) + " é possitivo")
else:
    print("O numero " + str(numero) + " é negativo")
'''

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''
sexo = input("Digite o sexo, F - Feminino, M - Masculino: ")

if sexo != "F" and sexo != "M":
    print("Sexo inválido!")
else:
    if sexo == "M":
        print("MASCULINO!")
    else:
        print("FEMININO!")
'''

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''
vogais=["a", "e", "i", "o", "u"]
letra= input("Digite uma letra: ")
for index in vogais:
    if index == letra:
        print("vogal")
        break
else:
    print("consoante")
'''

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular 
# a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
nota1= float(input("Digite a nota 1: "))
nota2= float(input("Digite a nota 2: "))

media = ((nota1 + nota2) / 2)

if media == 10:
    print("Aprovado com Distinção, media: " + str(media))
elif 7 < media < 10:
    print("Aprovado, media: " + str(media))
elif media < 7:
    print("Reprovado, media: " + str(media))
'''

#Faça um Programa que leia três números e mostre o maior deles.
'''
vetor=[]
for index in range(3):
    numero= int(input("digite um numero: "))
    vetor.append(numero)
print()
for index in range(len(vetor)):
    print(f'{index+1} numero digitado' f' {vetor[index]}')
    
print('O maior valor dos numeros é: ' f'{max(vetor)}')
'''

#Faça um Programa que leia três números e mostre o maior e o menor deles.

'''
numeros=[]
for index in range(3):
    elemento = int(input("Digite um numero: "))
    numeros.append(elemento)

print(f'O Maior numero digitado foi {max(numeros)}\n')
print(f'O Menor numero digitado foi {min(numeros)}')
'''

#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
#sabendo que a decisão é sempre pelo mais barato.
'''
precos=[]
for index in range(3):
    elemento= float(input('Digite o preco do produto: '))
    precos.append(elemento)

print(f'O produto mais economico custa R$ {min(precos)}')
'''

#Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
numeros=[]
for index in range(3):
    num= int(input("Digite um numero: "))
    numeros.append(num)

numeros.sort(key=int, reverse=True)

print(numeros)
'''
   
#Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" 
#ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''
entrada= False
nome= input("Qual o seu nome? ")
while entrada == False: 
    resposta= input('Em que turno você estuda? \nM - Matutino\nV - Vespertino\nN - Noturno\n')
    if resposta != 'M' and resposta != 'V' and resposta != 'N':
        print("Resposta invalida!")
    else:
        entrada= True

if resposta == 'M':
    print("Bom dia " f'{nome}!')
elif resposta == 'V':
    print("Boa tarde " f'{nome}!')
elif resposta == 'N':
    print("Boa noite " f'{nome}!')
'''

#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram 
#para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
#baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.
'''
salario = float(input("Qual é o valor do seu salário? "))
novo_salario = 0.00
if salario <= 280:
    novo_salario = salario * 1.2
elif salario <= 700:
    novo_salario = salario * 1.15
elif salario <= 1500:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.05

aumento = novo_salario - salario
percentual = round(((novo_salario / salario) - 1) * 100)

print(f'O salario original correspondia a R$ {salario}')
print(f'O percentual de aumento corresponde a {percentual}%')
print(f'O aumento foi de R$ {aumento}')
print(f'O novo salario corresponde a R$ {novo_salario}')
'''

#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do 
# Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato 
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário 
# o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
# dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#        Salário Bruto: (5 * 220)        : R$ 1100,00
#        (-) IR (5%)                     : R$   55,00  
#        (-) INSS ( 10%)                 : R$  110,00
#        FGTS (11%)                      : R$  121,00
#        Total de descontos              : R$  165,00
#        Salário Liquido                 : R$  935,00
'''
horas_trab= float(input("Quantas horas trabalhou no mes? "))
valor_hora= float(input("Qual é o valor pago por hora trabalhada? "))

#Calculo do Salario Bruto:
salario_bruto= horas_trab * valor_hora

#Calculo do Imposto de Renda:
if salario_bruto <= 900:
    ir = 0.00
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2

percent_ir = (ir / salario_bruto) * 100

#Calculo desconto Sindicato:
sindicato = salario_bruto * 0.03

#Calculo do valor do FGTS, no valor de 11%:
fgts = salario_bruto * 0.11

#Calculo do valor do INSS:
inss = salario_bruto * 0.1

#Calculo do total de descontos:
total_desc= sindicato + ir + inss
salario_liquido= salario_bruto - total_desc

print('')
print(f'Salario Bruto: (R$ {valor_hora} x {horas_trab})          :R$ {salario_bruto}')
print(f'(-) Sindicato: (3%)                      :R$ {sindicato}')
print(f'(-) Imposto de Renda: ({percent_ir}%)            :R$ {ir}')
print(f'(-) INSS: (10%)                          :R$ {inss}')
print(f'FGTS: (11%)                              :R$ {fgts}')
print(f'Total de descontos                       :R$ {total_desc}')
print(f'Salario Liquido                          :R$ {salario_liquido}')
'''

#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''
entrada = False
dias= ['1', '2', '3', '4', '5', '6', '7']
while entrada == False:
    valor = input("Digite um numero correspondente a um dia da semana:")
    for index in range(7):
        if valor == dias[index]:
            entrada=True
    if valor != dias[index]:
        print("Valor Inválido!!")

        
dias_semana= {
    '1' : 'Domingo',
    '2' : 'Segunda Feira',
    '3' : 'Terça Feira', 
    '4' : 'Quarta Feira',
    '5' : 'Quinta Feira',
    '6' : 'Sexta Feira',
    '7' : 'Sabado'
}        

escolha = dias_semana[valor]
print(escolha)
'''

#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao 
# longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
'''
nota1= float(input("Digite o valor da nota 1: "))
nota2= float(input("Digite o valor da nota 2: "))
media = (nota1 + nota2) / 2

#Verificação de conceito:
if media >= 9:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6.0:
    conceito = 'C'
elif media >= 4.0:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    situacao = "APROVADO"
else:
    situacao = "REPROVADO" 

print('')
print(f'Nota 1: {nota1}')
print(f'NOTA 2: {nota2}')
print(f'Media : {media}')
print(f'Conceito: {conceito} - {situacao}')
'''

#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores 
# podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, 
# isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;
'''
lado1 = float(input("Digite o lado 1 do triangulo: "))
lado2 = float(input("Digite o lado 2 do triangulo: "))
lado3 = float(input("Digite o lado 3 do triangulo: "))

print('')
if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print("Os lados informados formam um triangulo")
    triangulo = True
else:
    print("Os lados informados NAO formam um triangulo")
    triangulo = False

if triangulo == True:
    if lado1 == lado2 == lado3:
        print("Os lados correspondem a um triangulo Equilatero")
    elif lado1 != lado2 != lado3:
        print("Os lados correspondem a um triangulo Escaleno")
    else:
        print("Os lados correspondem a um triangulo Isósceles")
'''

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
# nas seguintes situações:
#>>Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa 
# não deve fazer pedir os demais valores, sendo encerrado;
#>>Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre 
# o programa;
#>>Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#>>Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

'''
valor_a = float(input("Digite o coeficiente A: "))
if valor_a == 0.0:
    exit()

valor_b = float(input("Digite o coeficiente B: "))
valor_c = float(input("Digite o coeficiente C: "))

delta = (valor_b * valor_b) - 4 * valor_a * valor_c

if delta < 0.00:
    print("A equação não possui raizes reais")
elif delta == 0.00:
    print("A equação possui apenas uma raiz real")
else:
    print("A equação possui duas raizes reais")
'''
#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe 
#se este ano é ou não bissexto.
'''
ano = int(input("Digite um ano: "))
if ano % 100 != 0:
    if ano % 4 == 0:  
        print("O ano é bissexto")
        exit()
    else:
        if ano % 400 == 0:
            print("O ano é bissexto")
            exit()

print("O ano NAO é bissexto")
'''

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
'''
meses = {
    'janeiro' : 31,
    'fevereiro' : 29,
    'março' : 31,
    'abril' : 30,
    'maio' : 31,
    'junho' : 30,
    'julho' : 31,
    'agosto' : 31,
    'setembro' : 30,
    'outubro' : 31,
    'novembro' : 30,
    'dezembro' : 31
}

#Função que verifica se o ano é bissexto:
def bissexto(ano):
    if (ano % 4) == 0:
        if (ano % 100) == 0:
            if (ano % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Solicitando entrada de data para o usuário:
data_correta = False

while data_correta == False:
    data = input("Digite uma data no seguinte formato dd/mm/aaaa: ")

    #Separando entrada do usuário em dia, mes e ano:
    data_dia = int(data[0:2])
    data_mes = int(data[2:4])
    data_ano = int(data[4:])

    #Verificando se o ano é bissexto:
    bissexto_check = bissexto(data_ano)

    #Validando entrada de dia, mes e ano:
    if data_ano > 9999 or data_ano <=0:
        print("Ano inválido")
    elif data_mes > 12 or data_mes <= 0:
        print("mes invalido")
    elif data_mes == 1 and data_dia > meses["janeiro"] or data_dia <=0:
        print("dia inválido")

    elif data_mes == 2 and bissexto_check == True:
        if data_dia > meses["fevereiro"] or data_dia <=0:
            print("dia inválido, ano bissexto")
        else:
            print(f'A data informada: {data_dia}/{data_mes}/{data_ano} esta CORRETA')    
            data_correta = True
    elif data_mes == 2 and bissexto_check == False:
        if data_dia > 28 or data_dia <=0:
            print("dia inválido, ano NAO bissexto")
        else:
            print(f'A data informada: {data_dia}/{data_mes}/{data_ano} esta CORRETA')
            data_correta = True

    elif data_mes == 3 and data_dia > meses["março"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 4 and data_dia > meses["abril"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 5 and data_dia > meses["maio"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 6 and data_dia > meses["junho"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 7 and data_dia > meses["julho"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 8 and data_dia > meses["agosto"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 9 and data_dia > meses["setembro"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 10 and data_dia > meses["outubro"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 11 and data_dia > meses["novembro"] or data_dia <=0:
        print("dia inválido")
    elif data_mes == 12 and data_dia > meses["dezembro"] or data_dia <=0:
        print("dia inválido")
    else:
        print(f'A data informada: {data_dia}/{data_mes}/{data_ano} esta CORRETA')
        data_correta = True
'''

#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
entrada = False
while entrada == False:
    numero = int(input("Digite um numero positivo menor que 1000: "))
    if numero >= 1000:
        print("Numero inválido, o valor deve ser inferior a 1000")
    elif numero < 0:
        print("Numero inválido, o numero deve ser positivo")
    else:
        entrada = True
        print("Numero correto")

numero_string = []
numero_string= str(numero)
separado = list(numero_string)

tamanho = len(separado)

if tamanho == 1:
    print(f'{numero_string} = {separado[0]} unidades')
elif tamanho == 2:
    print(f'{numero_string} = {separado[0]} Dezenas e {separado[1]} Unidades')
elif tamanho == 3:
    print(f'{numero_string} = {separado[0]} Centenas, {separado[1]} Dezenas e {separado[2]} Unidades')
'''

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas 
# notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais 
# e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, 
# uma nota de 5 e quatro notas de 1.

'''
print("Bem-vindo ao CAIXA ELETRONICO")
entrada = False
while entrada == False:
    valor = int(input("Quanto deseja sacar? "))
    if valor < 10:
        print("O valor minimo para saque é R$ 10.00")
    elif valor > 600:
        print("O valor máximo para saque é R$ 600.00")
    else:
        print("\nO saque esta sendo priocessado...\n")
        entrada = True

paga_cem = valor // 100
saldo1 = valor - (paga_cem * 100)

paga_ciquenta = saldo1 // 50
saldo2 = saldo1 - (paga_ciquenta * 50)

paga_dez = saldo2 // 10
saldo3 = saldo2 - (paga_dez * 10)

paga_cinco = saldo3 // 5
saldo4 = saldo3 - (paga_cinco * 5)

paga_um = saldo4

print("====================")
if paga_cem != 0:
    print(f'Notas de 100: {paga_cem}')
if paga_ciquenta != 0:
    print(f'Notas de 50: {paga_ciquenta}')
if paga_dez != 0:    
    print(f'Notas de 10: {paga_dez}')
if paga_cinco != 0:    
    print(f'Notas de 5: {paga_cinco}')
if paga_um != 0:
    print(f'Notas de 1: {paga_um}')
print("====================\n")
print("Saque efetuado com sucesso!!\n")
'''

#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).
'''
entrada = False
while entrada == False:
    numero= int(input("Informe um numero inteiro positivo, maior que zero:"))
    if not int(numero):
        print("O numero deve ser inteiro")
    elif int(numero) < 0:
        print("O numero deve ser positivo")
    elif numero == 0:
        print("O numero deve ser maior que zero")
    else:
        resultado = numero % 2
        if resultado == 0:
            print(f'O numero digitado {numero} é par')
        else:
            print(f'O numero digitado {numero} é impar')
        entrada = True
'''

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
#Dica: utilize uma função de arredondamento.

numero = float(input("Digite um numero: "))

arred_numero = round(numero)

if arred_numero - 




    
