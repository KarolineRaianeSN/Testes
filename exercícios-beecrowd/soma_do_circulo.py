def main():
    raio = float(input())  # float converte uma string em um número de ponto flutuante, app mais precisão
    area = 3.14159 * (raio ** 2)
    print(f"A={area:.4f}")


"""
a letra f indica que a string "A=" será interpolada com o valor da variável area. 
O caractere.4f indica que o valor de area será formatado como um número de ponto flutuante com quatro casas decimais.
"""
main()
