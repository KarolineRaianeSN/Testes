class Carro:
    def __init__(self, modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    def __str__(self):
        return f'{self.modelo}, {self.cor}, {self.ano}'

carro1 = Carro('novo', 'azul', 2024)

print(carro1)


class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Person:
    def __init__(self,name,age):
        super().__init__(name,age)
x = Student('Lia',20)

print(vars(x))

class Restaurante:
    def __init__(self, nome, categoria, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

# Exibindo uma instância do restaurante formatada
restaurante_formatado = Restaurante(nome='Bom Sabor', categoria='Tradicional')
print(restaurante_formatado)