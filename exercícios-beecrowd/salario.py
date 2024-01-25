def main():
    numero = int(input())
    valor = float(input())
    horas = float(input())

    salario = valor * horas

    print(f'NUMBER = {numero}')
    print(f'SALARY = U$ {salario:.2f}')


main()