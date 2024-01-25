def main():
    input()
    salario = float(input())
    vendas = float(input())

    comissao = vendas * 0.15
    salario_total = salario + comissao

    print(f'TOTAL = U$ {salario_total:.2f}')


main()
