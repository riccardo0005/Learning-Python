
#CREO UNA LISTA DI NUMERI LA LEGGO LA RIEMPIO CON CICLO E POI
#TROVO IL MAGGIORE E IL MINORE
print("Quanti numeri vuoi inserire? ")
numero = int(input())
listaNumeri = [] * numero #creo una lista di dimensione a scelta e vuota
print("Inserisci una lista di " + str(numero) + "numeri: ")
cont = 1
for i in range(numero):

    print("Numero " + str(cont) + " della lista: ")
    listaNumeri.append((input()))
    cont+=1
print("La lista inserita è: ")
for i in range(numero):
    print(listaNumeri[i])


minore = listaNumeri[0]
maxore = listaNumeri[0]   

for i in range(numero):

    if listaNumeri[i] < minore:
        minore = listaNumeri[i] 
    if listaNumeri[i] > maxore: 
        maxore = listaNumeri[i]

print("Il numero minore è: " + str(minore))
print("Il numero maggiore è: " + str(maxore))
