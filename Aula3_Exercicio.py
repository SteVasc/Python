'''
Exercicio: Pergunte a idade, altura e o peso de uma pessoa e informe se ela está apta para entrar no exercito.
 >=18 anos, >= de 60 kilos, >= 1,70 metros
'''

#Estruturas de Decisões IF/ELSE

peso = input("Digite seu peso: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

if idade >= ("18") and peso >= ("60") and altura >= ("1,70"):
    print("voce está apto para servir ao exercito")
else:
    print("você nao está apto para servir ao exercito")