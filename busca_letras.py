'''
1 - recebe uma palavra
2 - recebe uma letra pra buscar
3 - retorna quantas vezes a letra aparece e em quais posições
'''
print("Digite uma palavra: ")
txt = str(input())
print("Qual letra você deseja buscar na palavra?")
variavel = str(input())
txt_c = txt.count(variavel)
txt_i = txt.index(variavel)
posicoes = []
indice = 0
print("A letra", variavel, "foi encontrada", txt_c, "vezes")
print("A letra ",variavel,"foi encontrada nas posições:")
for indice in range(len(txt)):
    if txt[indice] == variavel:
            posicoes.append(indice + 1)
print(posicoes)
