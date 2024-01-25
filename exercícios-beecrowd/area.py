'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
'''
def main():

    a = float(input())
    b = float(input())
    c = float(input())

    area_triangulo = (a * c) / 2
    area_circulo = 3.14159 * (c ** 2)
    area_trapezio = (a + b) * c / 2
    area_quadrado = (b * b)
    area_retangulo = (a * b)

    print(f'TRIANGULO: {area_triangulo:.3f}')
    print(f'CIRCULO: {area_circulo:.3f}')
    print(f'TRAPEZIO: {area_trapezio:.3f}')
    print(f'QUADRADO: {area_quadrado:.3f}')
    print(f'RETANGULO: {area_retangulo:.3f}')

if __name__ == '__main__':
    main()