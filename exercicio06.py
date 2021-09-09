print ("Bem-Vindo a nossa loja online de computadores!")

lista = []

print ("\nAlguns itens foram adicionados a sua lista")
item1 = input("O que mais você precisa para seu INCRÍVEL pc gamer: ")
lista = [item1]

lista.insert(0,"Gabinete cooler master")
lista.insert(1,"placa de vídeo GeForce RTX 2080Ti")
print (lista)

#A
print ("OPS! Parece que você não consegue comprar os itens desejados.")

del lista[1]
del lista[0]

print ("Retiramos dois itens para que você consiga efetuar o pagamento")
print ("Aqui estão os itens que você consegue comprar",lista)