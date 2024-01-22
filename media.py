'''
Calcular a média de uma lista de números: Este exercício envolve a criação de um programa que recebe uma lista de números como entrada e calcula a média dos valores presentes na lista
'''
import os

numeros = []
def exibir_menu():
    print("Menu principal")
    print("[ 1 ] - Adicionar numero na lista")
    print("[ 2 ] - Mostrar média dos números")
    print("[ 3 ] - Encerrar")


def cadastrar_numeros():
    numero_adicionado = int(input('Digite um número novo: '))
    numeros.append(numero_adicionado)
    print(numeros)
    cadastrar_novo_numero()


def opção_invalida():
        print('Opção inválida!\n')
        cadastrar_novo_numero()


def encerrar():
    os.system('cls')
    print('Programa encerrado')


def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        cadastrar_numeros()
    if opcao_escolhida == 2:
        calcular_media()
    if opcao_escolhida == 3:
        encerrar()
    else:
        opção_invalida()


def calcular_media():
    if sum(numeros) == 0:
        print('Adicione números na lista!')
    else:
        soma = sum(numeros)
        quantidade = len(numeros)

        media = soma / quantidade

        print(f'A média dos números adicionados é igual a {media}')
        cadastrar_novo_numero()


def cadastrar_novo_numero():
    input('\nDigite uma tecla para voltar para o menu principal')
    main()


def exibir_subtitulo(texto):
    os.system('cls')


def opcao_invalida():
    print('Opção inválida!\n')
    cadastrar_novo_numero()


def main():
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()


