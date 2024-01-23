'''
    dados:
        nome
        cpf
            validar cpf
        saldo
    funções:


    - cadastro: nome, cpf e saldo
    - consulta: informar cpf e retornar saldo
    depósito
    - transferência:tranfere saldo entre clientes e informar se o saldo é suficiente
    - voltar ao menu iniciar


    "telas"
    - menu inicial
    - consulta: nome, cpf e saldo
    - cpf invalido
    - saldo insuficiente: retorna saldo em conta
    - tranferencia realizada
'''


def menu_principal():
    print("🅐🅖🅘🅞🅣🅐'🅢 🅑🅐🅝🅚")
    print('[1] - Novo cadastro')
    print('[2] - Consulta com CPF')
    print('[3] - Depósito')
    print('[4] - Transferência')
    print('[5] - Sair')



clientes = [{'nome':'Karoline Raiane', 'cpf':61231680377, 'saldo': 0}, {'nome': 'Nelita Machado', 'cpf': 47926597368, 'saldo':1000}]
cpfs = ()


def escolha_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastro()
        elif opcao_escolhida == 2:
            consulta()
        elif opcao_escolhida == 3:
            deposito()
        elif opcao_escolhida == 4:
            debito_em_conta()
        elif opcao_escolhida == 5:
            sair()
        else:
            print('Opção inválida!')
    except Exception as erro:
        print('Opção inválida')


def consulta():
    documento = int(input('Digite um CPF: '))
    for indice in clientes:
        if documento == indice['cpf']:
            print(indice['nome'])
            print(indice['saldo'])
    input('\nDigite uma tecla para voltar para o menu principal')
    main()


def debito_em_conta():
    cliente_origem = input('Insira seu nome: ')
    for indice in clientes:
        if cliente_origem == indice['nome']:
            valor_transferido = float(input('Digite o valor que deseja depositar: '))
            if valor_transferido <= indice['saldo']:
                saldo_origem_atual = indice['saldo'] = indice['saldo'] - valor_transferido
                print(indice['saldo'])
            else:
                print('Saldo insuficiente')
    cliente_destino = input('Digite pra quem você deseja transferir: ')
    for index in clientes:
        if cliente_destino == index['nome']:
            saldo_destino_atual = index['saldo'] = index['saldo'] + valor_transferido
    input('\nDigite uma tecla para voltar para o menu principal')
    main()


def transferencia_realizada():
    pass


def sair():
    print('Transação encerrada')


def cadastro():
    novo_cpf = int(input('Digite seu cpf: '))
    for indice in clientes:
        if novo_cpf == indice['cpf']:
            print('CPF já cadastrado')
            cadastro()

    novo_cliente = input('Digite Seu nome: ')
    saldo_inicial = float(input('Digite seu saldo: '))
    dados_novo_cliente = {'nome': novo_cliente, 'cpf': novo_cpf, 'saldo': saldo_inicial}
    clientes.append(dados_novo_cliente)
    input('\nDigite uma tecla para voltar para o menu principal')
    main()


def deposito():
    cliente = input('Digite seu nome: ')
    for indice in clientes:
        if cliente == indice['nome']:
            deposito = float(input('Digite o valor que deseja depositar: '))
            saldo_atual = indice['saldo'] = indice['saldo'] + deposito
    input('\nDigite uma tecla para voltar para o menu principal')
    main()


def main():
    if __name__ == "__main__":
        menu_principal()
        escolha_opcao()
main()
