
# Bibliotecas
import time

# Função para converter unidades de massa
def converterMassa(unidade_inicial, unidade_final, valor):
    # Medidas de massa
    medidas_massa = {
        "g": 1,
        "kg": 1000,
        "mg": 0.001,
        "lb": 453.592,
        "oz": 28.3495
    }

    # Verifica se as unidades passadas são válidas
    if unidade_inicial in medidas_massa and unidade_final in medidas_massa:
        # Calcula a conversão
        resultado = (medidas_massa[unidade_final] / medidas_massa[unidade_inicial]) * valor
        # Exibe o resultado
        print("O resultado da conversão é: {:.2f}".format(resultado))
    else:
        print("Unidade não suportada.")

# Função para converter unidades de tempo
def converterTempo(unidade_inicial, unidade_final, valor):
    # Medidas de tempo
    medidas_tempo = {
        "s": 1,
        "min": 60,
        "h": 3600,
        "d": 86400
    }

    # Verifica se as unidades passadas são válidas
    if unidade_inicial in medidas_tempo and unidade_final in medidas_tempo:
        # Calcula a conversão
        resultado = (medidas_tempo[unidade_final] / medidas_tempo[unidade_inicial]) * valor
        # Exibe o resultado
        print("O resultado da conversão é: {:.2f}".format(resultado))
    else:
        print("Unidade não suportada.")

# Função para converter unidades de volume
def converterVolume(unidade_inicial, unidade_final, valor):
    # Medidas de volume
    medidas_volume = {
        "ml": 1,
        "l": 1000,
        "gal": 3785.41
    }

    # Verifica se as unidades passadas são válidas
    if unidade_inicial in medidas_volume and unidade_final in medidas_volume:
        # Calcula a conversão
        resultado = (medidas_volume[unidade_final] / medidas_volume[unidade_inicial]) * valor
        # Exibe o resultado
        print("O resultado da conversão é: {:.2f}".format(resultado))
    else:
        print("Unidade não suportada.")

# Função para converter unidades
def converterUnidade(unidade_inicial, unidade_final, valor):
    # Verifica qual tipo de unidade foi passado
    if unidade_inicial[-1] == "g" or unidade_final[-1] == "g":
        converterMassa(unidade_inicial, unidade_final, valor)
    elif unidade_inicial[-1] == "l" or unidade_final[-1] == "l":
        converterVolume(unidade_inicial, unidade_final, valor)
    elif unidade_inicial[-1] == "s" or unidade_final[-1] == "s":
        converterTempo(unidade_inicial, unidade_final, valor)
    else:
        print("Unidade não suportada.")

# Entrada de dados
unidade_inicial = input("Digite a unidade inicial (ex: kg, l, s): ")
unidade_final = input("Digite a unidade final (ex: g, ml, min): ")
valor = float(input("Digite o valor a ser convertido: "))

# Executa a função
converterUnidade(unidade_inicial, unidade_final, valor)
