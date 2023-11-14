#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
#print("hello world")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
#numero = input("digite um numero: ")
#print("o numero escolhido foi: " + str(numero))

#Faça um Programa que peça dois números e imprima a soma.
'''
def soma(num1, num2):
    result = (num1 + num2)
    return result
'''

'''
while True:
    numero1= input("digite um numero: ")
    if numero1.isdigit():
        numero1= float(numero1)
    else:
        print("Entrada inválida")
    numero2= input("digite outro numero: ")
    if numero2.isdigit():
        numero2= float(numero2)
        break
    else:
        print("Entrada inválida")
        break

resultado= (float(numero1) + float(numero2))
print("A soma dos dois numeros é: " + str(resultado))
'''

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''
nota1= input("digite a nota 1: ")
nota2= input("digite a nota 2: ")
nota3= input("digite a nota 3: ")
nota4= input("digite a nota 4: ")
media=((float(nota1)+float(nota2)+float(nota3)+float(nota4))/4)
print("A media das notas é: " + str(media))
'''
#Falta Finalizar:
'''
notas=[12, 23, 43, 21]
soma = 0
for index in range(notas):

    soma =+ notas[index]
print(soma)
'''

#Faça um Programa que converta metros para centímetros.
'''
def convert_m_cm(valor):
    resultado=(float(valor) * 100)
    return resultado

metro= input("Digite o valor em metros: ")
convertido= convert_m_cm(metro)
print("valor convertido em centimetros: " + str(convertido))
'''

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
pi= 2.14
raio= input("Digite o valor do raio do circulo: ")

area= pi * (float(raio)* float(raio))
print("A área do circulo é: " + str(area))
'''

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''
lado= input("digite o valor do lado do quadruado: ")
resultado= (float(lado) * float(lado)) * 2
print("O dobro do da área do quadrado é: " + str(resultado))
'''

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
'''
ganho_hora= input("Quanto você ganha por hora trabalhada?: ")
hora_mes= input("Quantas horas trabalhou no mês?: ")
resultado= float(ganho_hora) * float(hora_mes)
print("Teu salario do mes equivale a: " + str(resultado))
'''

#Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
'''
fahrenheit = input("Digite a temperatura em Fahrenheit: ")
resultado = 5 * ((float(fahrenheit) - 32) / 9)
print("A temperatura em Celcius coresponde a: " + str(resultado))
'''

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
'''
inteiro1= int(input("digite um numero inteiro: "))
inteiro2= int(input("digite outro numero inteiro: "))
real1= float(input("digite um numero real: "))

resultado1=(inteiro1 * 2) * (inteiro2 / 2)
resultado2=(inteiro1 * 3) + real1
resultado3=(real1 * real1 * real1)

print("o produto do dobro do primeiro com metade do segundo: " + str(resultado1))
print("#a soma do triplo do primeiro com o terceiro: " + str(resultado2))
print("#o terceiro elevado ao cubo: " + str(resultado3))
'''

#Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
'''
altura= float(input("Digite a sua altura: "))
ideal= (72.7 * altura) - 58
print("Seu peso ideal é: " + str(ideal))
'''

#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
'''
altura= float(input("Digite a altura: "))
genero = input("Digite seu genero (H: Homem / M: Mulher): ")

if genero == "H" or genero == "h":
    ideal_h = (72.7 * altura) - 58
    print("Altura ideal para homem: " + str(ideal_h))
else:
    ideal_m = (62.1 * altura) - 44.7
    print("Altura ideal para mulher: " + str(ideal_m))
'''

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
#diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
#excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) 
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
#e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa 
#com as mensagens adequadas.
'''
limite = 50
pesca= float(input("Quantos quilos pescou? "))

if pesca > limite:
    exceso= pesca - limite
    multa= exceso * 4
    print("O valor da multa corresponde a: " + str(multa))
else:
    print("Não há multa!")
'''

'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.


salario_hora= input("Digite seu salario por hora: ")
horas_trabalhadas= input("Quantas horas trabalhou no mês?: ")

salario_bruto= float(salario_hora) * float(horas_trabalhadas)
ir= salario_bruto * (11 / 100)
inss= salario_bruto * (8 / 100)
sindicato= salario_bruto * (5 /100)

descontos= ir + inss + sindicato
liquido= salario_bruto - descontos

print("Salario Bruto corresponde: " + str(salario_bruto))
print("Valor pago de IR corresponde a: ", str(ir))
print("Valor pago de INSS corresponde a: ", str(inss))
print("Valor pago de Sindicato corresponde a: ", str(sindicato))
print("Salario Liquido corresponde: ", str(liquido))
'''

#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades 
# de latas de tinta a serem compradas e o preço total.
'''
import math
desempenho= 3
capacidade_lata = 18.00
preco_lata = 80.00

tamanho_metros= input("Quantos metros quadrados deseja pintar? ")
necessidade= float(tamanho_metros) / desempenho
print("Precisa de " + str(necessidade) + " litros de tinta")
latas= float(necessidade) / float(capacidade_lata)
latas_total = math.ceil(latas)
latas_valor = latas_total * preco_lata 
print("Precisa de " + str(latas_total) + " latas de tinta")
print("O valor total a pagar corresponde: " + str(latas_valor))
'''

#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, 
#isto é, considere latas cheias.
'''
import math
cobertura = 6.00 # cobertura de 6 metros quadrados por litro de tinta
lata= 18.00 # litros por lata
galao= 3.60 #litros por galao
lata_18_preco = 80.00
galao_36_preco = 25.00

necessidade = input("Quantos metros quadrados deseja pintar? ")
tinta_necessaria= (float(necessidade) / cobertura)
print("A quantidade de tinta a ser utilizada é: " + str(tinta_necessaria))

total_lata= math.ceil(tinta_necessaria / lata)
total_lata_preco = total_lata * lata_18_preco
total_galao= math.ceil(tinta_necessaria / galao)
total_galao_preco = total_galao * galao_36_preco

if  tinta_necessaria < lata:
    #print("É recomendado comprar apenas latas de 18 litros")
    print("Precisa de " + str(total_lata) + " lata") 
    print("O valor total corresponde a: R$ " + str(total_lata_preco))
else:
    excedente= (tinta_necessaria % lata) * 1.1
    lata18 = tinta_necessaria / lata
    lata18 = math.floor(lata18)
    galao_excedente = math.ceil(excedente / galao)
    if galao_excedente > 3:
        print("Fica mais econimico comprar " + str(total_lata) + " lata/s")
        print("Valor total R$ " + str((total_lata)* lata_18_preco))
    else:
        print("Fica mais economico comprar " + str(lata18) + " lata/s e " + str(galao_excedente) + " galao/es")
        print("Valor total R$: " + str((lata18 * lata_18_preco)+(galao_excedente * galao_36_preco)))
'''

#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

'''
tamanho= float(input("Qual é o tamanho do arquivo para download? em MB: "))
velocidade= float(input("Qual é a velocidade da internet? em MBps: "))

resultado= tamanho / (velocidade * 60)
print("O tempo aproximado para download é: " + str(resultado) + " minutos")
'''




















    











