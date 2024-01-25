def main():

    lanches = [{'codigo': 1, 'especificacao' : 'cachorro-quente', 'preco' : 4.00}, {'codigo': 2, 'especificacao'
    :'x-salada', 'preco' : 4.50}, {'codigo': 3, 'especificacao' : 'x-bacon', 'preco' : 5.00}, {'codigo': 4,'especificacao'
    :'torrada simples','preco' : 2.00},{'codigo': 5, 'especificacao' : 'refrigerante', 'preco' : 1.50}]

    codigo = int(input('Insira o código do produto: '))
    quantidade = int(input('Insira a quantidade que deseja comprar: '))

    for indice in lanches:
        if codigo == indice['codigo']:
            total = indice['preco'] * quantidade
            print(f'Total = R$ {total:.2f}')

if __name__ == '__main__':
    main()