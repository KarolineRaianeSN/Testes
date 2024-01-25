'''
Escreva um programa que repita a leitura de uma senha até que ela seja válida. Para cada leitura de senha incorreta informada, escrever a mensagem "Senha Invalida". Quando a senha for informada corretamente deve ser impressa a mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha correta é o valor 2002.

Entrada
A entrada é composta por vários casos de testes contendo valores inteiros.

Saída
Para cada valor lido mostre a mensagem correspondente à descrição do problema.
'''


#Inserir senha
#Enquanto
#Comparar senha com números randomicos
#Retornar senha inválida se n for e acesso permitido se for igual

import random
def main():

    senhas = set([])

    senha_correta = 2024

    for indice in range(10000):
        senhas.add(random.randrange(0000,9999))
        if senha_correta in senhas:
            print("Acesso permitido")
            break
        print('Acesso negado!')

if __name__ == "__main__":
    main()

