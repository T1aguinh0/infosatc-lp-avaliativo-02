item1 = input("Adicione um item na lista: ")
item2 = input("Adicione um item na lista: ")
item3 = input("Adicione um item na lista: ")
 
lista = [item1, item2, item3]
 
verificar = input("Deseja verificar qual item? ")
 
if verificar in lista:
    print("O item ESTÁ na lista")
else:
    print("O item NÃO ESTÁ na lista")