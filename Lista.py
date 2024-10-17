# 1. Soma de dois números
# Peça ao usuário dois números e mostre a soma deles.
print('Soma de dois números\n')
n1 = int(input('Informe o número 1: '))
n2 = int(input('Informe o número 2: '))
soma = n1+n2 
print(f'Soma de dois números:{soma} \n')


# 2. Subtração de dois números
# Peça ao usuário dois números e mostre a subtração primeiro pelo segundo.
print('Subtração de dois números\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
subtracao = n1-n2  
print('Subtração de dois números:',subtracao,'\n')


# 3. Multiplicação de dois números
# Peça ao usuário dois números  e moste o resultado da multiplicação entre eles.
print('Multiplicação de dois números\n')
n1 = int(input('Informe o número 1: '))
n2 = int(input('Informe o número 2: '))
multiplicacao = n1*n2 
print('Multiplicação de dois números:',multiplicacao,'\n')


# 4. Divisão de dois números
# Peça ao usuário dois números e mostre o resultado da divisão do primeiro pelo segundo
print('Divisão de dois números\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
divisao = n1/n2 
print('Divisão de dois números:',divisao,'\n')


# 5. Resto da divisão de dois números
# Peça ao usuário dois números e mostre o resto da divisão ente eles.
print('Resto de dois números\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
resto = n1%n2 
print('resto da divisão de dois números:' ,resto,'\n')


# 6. Potencia de um número
# Peça ao usuário um número e um expoente e mostre o resultado do número elevado ao expoente.
print('Potencia de um número\n')
n1 = int(input('Informe o número 1: '))
expoente = 2
potencia = n1**2 
print('Potencia de dois números:' ,potencia,'\n')


#7. Média de três números
# Peça ao usuário três números e mostre a média deles.
print('Média de três números\n')
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
soma = n1+n2+n3
media = soma/3 
print(f'Média da divisão de dois números: {media}')


#8. Conversão da temperatura
#Converta uma temperatura em graus Celsius para Fahrenheit usando a formula:
# F=95C+32F=\frac{9}{5} + 32F=59C+32
print('Conversão da temperatura\n')
temp_em_celcius = float(input('Mostre a temperatura em °C: '))
temp_em_fahrenheit = (9/5 * temp_em_celcius) + 32
print(f'Mostre a temperatura em °F é: {temp_em_fahrenheit}\n')


# 9.Conversão de moeda
#Peça um valor em reais e mostre o valor convertido em doláres.
#Considere uma taxa de conversão fixa.
print('Conversão da moeda\n')
valor_em_reais = float(input('Mostre o valor em Reais R$: '))
taxa_de_conversão = 5
valor_convertido_dolares = valor_em_reais/taxa_de_conversão
print(f'O valor em dólar é: {valor_convertido_dolares}\n')


# 10. Área de um Retângulo
#Peça a largura e altura de retângulo e calule a área
print('Área de um Retângulo\n')
largura_de_retangulo = float(input('Mostre a largura do retângulo: '))
altura_do_retangulo = float(input('Mostre a altura do retângulo: '))
area_do_retangulo = largura_de_retangulo * altura_do_retangulo
print(f'Calcule a área do retângulo: {area_do_retangulo}\n')


# 11. Perímetro de um quadrado
# Peça um lado de quadrado e calcule o perímetro (soma dos lados)
print('Perímetro de Um Quadrado\n')
lado_do_quadrado = float(input('Mostre o lado do quadrado: '))
perimetro_do_quadrado = lado_do_quadrado * 4
print(f'Calcule o perímetro do quadrado: {perimetro_do_quadrado}\n')


# 12. Área de Um Triângulo
# Peça a base e a altura de um triangulo e calcule a área usando a fórmula:
# Área=base*altura\text{Área}\frac{\tex{base}\times\text{altura}}{2}Área=basexaltura
print('Área de um Triângulo\n')
base_do_triangulo = float(input('Mostre a base do triângulo: '))
altura_do_triangulo = float(input('Mostre a altura do triângulo: '))
area_do_triangulo = (base_do_triangulo * altura_do_triangulo)/2
print(f'Calcule a área do triângulo: {area_do_triangulo}\n')


# 13. Área de um circulo
# Peça o raio de um círculo e calcule a área usando a formula:
# Área=πr2\text{Área}=\πr^2Área=πr2
# (Use o valor aproximado de π=3.14159).
print('Área de um Círculo\n')
raio_do_circulo = float(input('Mostre o raio do círculo: '))
PI = 3.14159
area_do_circulo = PI * (raio_do_circulo**2)
print(f'Calcule a área do círculo: {area_do_circulo:.3f}\n')


# 14. Conversão de metros para centimetros
# Peça um valor em metros e converta para centímetros.
print('Conversão de metros para centímetros\n')
valor_em_metros = float(input('Mostre o valor em metros: '))
valor_em_centimetros = valor_em_metros * 100
print(f'Mostre o valor em centímetros: {valor_em_centimetros}\n')


# 15. Cálculo de horas de trabalho
# Peça a quantidade de horas de trabalhadas e o valor por hora, e calcule o salário total.
print('Cálculo de horas de trabalho\n')
horas_trabalhadas = float(input('Mostre a quantidade de horas trabalhadas: '))
valor_por_hora = float(input('Mostre o valor por hora: '))
salario_total = horas_trabalhadas * valor_por_hora
print(f'Calcule o salário total: {salario_total}\n')


# 16. Preço com desconto
# Peça o preço de um produto e o percentual de desconto, e mostre o preço final
#com desconto aplicado.
print('Preço com desconto\n')
produto = float(input('Mostre o preço do produto R$: '))
desconto = float(input('Mostre o percentual de desconto: '))
preco_final = produto - (produto * (desconto / 100))
print(f'Mostre o preço final com desconto: {preco_final:.2f}\n')


# 17. Calcular a velocidade Média
# Peça a distância percorrida e o tempo gasto, calcule a velocidade média usando a formula:
# v=distânciatempov=\frac{\text{distância}}{\text{tempo}}v=tempodistancia
print('Calcular a velocidade Média\n')
distancia_percorrida = float(input('Mostre a distância percorrida KM: '))
tempo_gasto = float(input('Mostre o tempo gasto h: '))
velocidade_media = distancia_percorrida / tempo_gasto
print(f'Calcule a velocidade média: {velocidade_media:.2f}\n')


# 18. Converter idade em dias
# Peça a idade de uma pessoa em anos e converta para dias.
# (Desconsidere os anos bissextos)
print('Converter idade em dias\n')
idade_em_anos = int(input('Mostre a idade em anos: '))
idade_em_dias = idade_em_anos * 365
print(f'Mostre a idade em dias: {idade_em_dias}\n')


# 19 Quantidades de segundos em um dia
# Calcule quantos segundos existem e um dia (24 horas)
print('Quantidades de segundos em um dia\n')
segundos_em_um_dia = 24 * 60 * 60
print(f'Calcule quantos segundos existem em um dia: {segundos_em_um_dia}\n')


# 20. Calcular o IMC (Indice de Massa Corporal)
# Peça  o peso (em Kg) e a altura (em metros), e calcule o IMC usando a formula:
#IMC = pesoaltura2\text{IMC}=\frac{\text{peso}}{\text{altura}^2}IMC=altura2peso
print('Calcular o IMC\n')
peso = float(input('Mostre o peso em Kg: '))
altura = float(input('Mostre a altura em metros: '))
imc = peso / (altura ** 2)
print(f'Calcule o IMC: {imc:.2f}\n')


# 21. Diferença entre dois números
# Peça dois números inteiros e mostre a diferença absoluta entre eles (sem considerar resto)
print('Diferença entre dois números\n')
n1 = int(input('Mostre o primeiro número: '))
n2 = int(input('Mostre o segundo número: '))
diferenca_absoluta = abs(n1 - n2)
print(f'Mostre a diferença absoluta entre eles: {diferenca_absoluta}\n')


# 22. Divisão inteira de dois números
# Peça dois números inteiros e mostre o resultado da divisão inteira (sem considerar o resto)
print('Divisão inteira de dois números\n')
n1 = int(input('Mostre o primeiro número: '))
n2 = int(input('Mostre o segundo número: '))
divisao_inteira = n1 // n2
print(f'Mostre o resultado da divisão inteira: {divisao_inteira}\n')


# 23. Valor absoluto de um número
# Peça o um número e mostre se valor absoluto.
print('Valor absoluto de um número\n')
n1 = float(input('Mostre o número: '))
valor_absoluto = abs(n1)
print(f'Mostre o valor absoluto: {valor_absoluto}\n')


# 24 Converter km/h para m/s
# Peça uma velocidade em km/h e converta para m/s. Use a fórmula:
# velocidade em m/s=velocidade em km/h/3.6\text{velocidade em m/s}=\frac{\text{velocidade em km/h}}{3.6}velocidade em m/s=velocidade em km/h
print('Converter km/h para m/s\n')
velocidade_em_km_hora = float(input('Mostre a velocidade em km/h: '))
velocidade_em_m_segundos = velocidade_em_km_hora / 3.6
print(f'Mostre a velocidade em m/s: {velocidade_em_m_segundos:.2f}\n')


# 25. Fórmula de Bhaskara
# Peça os coeficientes aaa, bbb e ccc de uma equação do segundo grau e calcule as raízes usando a formula de Bhaskara.
print('Fórmula de Bhaskara\n')
coeficientes_aaa = float(input('Mostre o coeficiente aaa: '))
coeficientes_bbb = float(input('Mostre o coeficiente bbb: '))
coeficientes_ccc = float(input('Mostre o coeficiente ccc: '))
delta = (coeficientes_bbb ** 2) - (4 * coeficientes_aaa * coeficientes_ccc)
raiz_delta = delta ** 0.5
raiz1 = (-coeficientes_bbb + raiz_delta) / (2 * coeficientes_aaa)
raiz2 = (-coeficientes_bbb - raiz_delta) / (2 * coeficientes_aaa) 
print(f'Calcule as raízes da equação: {raiz1:.3f} e {raiz2:.3f}\n') 


# 26. Valor total de uma compra
# Peça o preço de três produtos e calcule o valor total da compra
print('Valor total de uma compra\n')
produto1 = float(input('Mostre o preço do primeiro produto R$: '))
produto2 = float(input('Mostre o preço do segundo produto R$: '))
produto3 = float(input('Mostre o preço do terceiro produto R$: '))
valor_total = produto1 + produto2 + produto3
print(f'Calcule o valor total da compra R$: {valor_total:.2f}\n')

# 27. Converte dias para semanas e dias
# Peça um valor em dias e converta para semanas e dia (por exemplo, 10 dias = 1 semana e 3 dias).
print('Converte dias para semanas e dias\n')
dias = int(input('Mostre o valor em dias: '))
semanas = dias // 7
dias_restantes = dias % 7
print(f'Mostre o valor em semanas e dias: {semanas} semanas e {dias_restantes} dias\n')


# 28. Desconto progressivo
# Peça o valor de uma compra e aplique um desconto 5% se o valor for maior que R$ 100 e de 10% se for maior que R$ 500.
valor_da_compra = float(input('Mostre o valor da compra R$: '))
if valor_da_compra > 500:
    desconto = 0.1
    valor_com_desconto = valor_da_compra - (valor_da_compra * desconto)
    print(f'Mostre o valor com desconto R$: {valor_com_desconto:.2f}\n')
elif valor_da_compra > 100 and valor_da_compra <= 500:
    desconto = 0.05
    valor_com_desconto = valor_da_compra - (valor_da_compra * desconto)
    print(f'Mostre o valor com desconto R$: {valor_com_desconto:.2f}\n')
else: valor_da_compra <= 100
desconto = 0
print(f'Mostre o valor da compra R$: {valor_da_compra:.2f}\n')
    

# 29. Divisão com casas decimais limitadas
# Peça dois números e mostre o resultado da divisão com apenas duas casas decimais.
print('Divisão com casas decimais limitadas\n')
n1 = float(input('Mostre o primeiro número: '))
n2 = float(input('Mostre o segundo número: '))
divisao = n1 / n2
print(f'Mostre o resultado da divisão com apenas duas casas decimais: {divisao:.2f}\n')

