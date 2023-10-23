# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
print("Calculador de aumento")
salario = float(input("Digite o valor do seu salário atual: "))
if salario > 1250:
    print(f"O seu salário agora será de {salario+(salario*(10/100))}")
else:
    print(f"O seu salário agora será de {salario+(salario*(15/100))}")