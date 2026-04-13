from calculadora.calculator import encontrar_raizes, calcular_media
# Importando funcoes

# Valores definidos para o calculo
valores = [1, 2, 3, 4]
lista_coeficientes = [1, -5, 6]

# Definindo funcao principal
def main():

    media = calcular_media(valores)
    raizes = encontrar_raizes(lista_coeficientes)

# Mostrando resultados
    print(f'Media Calculada: {media}')
    print(f'Raizes Encontradas: {raizes}')

# Interruptor
if __name__ == "__main__":
    main()