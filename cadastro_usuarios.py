'''
- Declarar dicionário
- Ler informações do dicionário
- Armazenar informações no dicionário
- Exibir informações do dicionário
'''

usuarios = [{"nome": "João","idade": 25,"cidade": "São Paulo"}]

nome = input('Digite o nume de um usuário: ')
idade = int(input('Digite a idade do usuário: '))
cidade = input('Digite a cidade do usuário: ')
altura = float(input('Digite a altura do usuário: '))
adicionar_dicionario = {'nome': nome, 'idade':idade, 'cidade':cidade, 'altura':altura}
usuarios.append(adicionar_dicionario)

for usuario in usuarios:
    print(usuario)