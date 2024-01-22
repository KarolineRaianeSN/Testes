#TESTANDO FUNÇÕES

''' TESTE 1 - Dada uma string, escreva um código para converter todas as letras maiúsculas para minúsculas.'''

txt = "TEXTO COM LETRAS MINUSCULAS"
txt_l = txt.lower()
print(txt_l)

'''TESTE 2 - Dada uma string, escreva um código para converter todas as letras minúsculas para maiúsculas.'''

txt1 = "TEXTO EM LETRAS MAIUSCULAS"
txt_u = txt1.upper()
print(txt_u)

'''TESTE 3 - Dada uma string, escreva um código para remover todas as aspas.'''
#strip()
#Remove todos os caracteres especificados do início e do fim da string.

txt2 = ".Olá, .mundo!. é um .país. bonito."
txt_sem_aspas = txt2.strip(".")
print(txt_sem_aspas)

'''TESTE 4 - Dada uma string, escreva um código para substituir todas as ocorrências de um caractere por outro caractere.'''

txt3 = "Olá, mundo!"
txt_r = txt3.replace("Olá" , "Tchau")
print(txt_r)

'''TESTE 5 - Dada uma string, escreva um código para contar o número de vezes que um caractere aparece na string.'''
#string.count(value, start, end)
txt4 = str(input())
variavel = str(input())
txt_c = txt4.count(variavel)
indice = 0
while indice != -1:
    indice = txt4.find("a", indice)
    print(indice)
    print("A letra a foi encontrada {} vezes, nas posições {}.".format(txt_c, indice))
    indice = indice + 1