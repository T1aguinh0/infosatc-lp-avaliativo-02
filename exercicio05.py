#A
filme1 = input("Adicione um item para a lista de filmes: ")
filme2 = input("Adicione um item para a lista de filmes: ")

lista_filmes = [filme1,filme2]

#a
lista_filmes.append("Avatar")
lista_filmes.insert(2,"Transformers")

print ("Sua lista de filmes",lista_filmes)

#B
jogo1 = input("Adicione um item para a lista de jogos: ")
jogo2 = input("Adicione um item para a lista de jogos: ")

lista_jogos = [jogo1,jogo2]

#a
lista_jogos.append("Fortnite")
lista_jogos.insert(4,"Uncharted")

print ("Sua lista de jogos",lista_jogos)

#C
livro1 = input("Adicione um item para a lista de livros: ")
livro2 = input("Adicione um item para a lista de livros: ")

lista_livros = [livro1,livro2]

#a
lista_livros.append("Pequeno Príncipe")
lista_livros.insert(0,"A Menina que Roubava Livros")

print ("Sua lista de livros",lista_livros)

#D
esporte1 = input("Adicione um item para a lista de esportes: ")
esporte2 = input("Adicione um item para a lista de esportes: ")

lista_esportes = [esporte1,esporte2]

#a
lista_esportes.insert(1,"Futsal")
lista_esportes.append("Rugbi")

print ("Sua lista de esportes",lista_esportes)

#b
lista_total = lista_filmes + lista_jogos + lista_livros + lista_esportes
print("Itens de todas as listas juntos",lista_total)

#c
print(lista_livros[2])

#d
del lista_esportes[3]
print(lista_esportes)


