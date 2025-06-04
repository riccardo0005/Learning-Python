# Scrivi un programma che a partire da un elemento e una lista di elementi dica in output se 
# l'elemento passato sia presente o meno nella lista.
# Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento tramite il metodo index.

import random  # Importa il modulo random per generare numeri casuali

listaNumeri = []  # Crea una lista vuota che conterrà i numeri generati casualmente

print("Quanti numeri vuoi inserire nella lista?")  # Chiede all'utente quanti numeri vuole nella lista
numeroElementi = int(input())  # Legge il numero di elementi da inserire e lo converte in intero

for i in range(numeroElementi):  # Cicla per il numero di elementi richiesto
    numero = random.randint(1, 10000)  # Genera un numero casuale tra 1 e 10000
    listaNumeri.append(numero)  # Aggiunge il numero generato alla lista

print("Inserisci un numero da cercare nella lista e ti verrà restituita la sua posizione se è presente:")  # Chiede all'utente quale numero cercare
numeroDaCercare = int(input())  # Legge il numero da cercare e lo converte in intero

if numeroDaCercare in listaNumeri:  # Controlla se il numero è presente nella lista
    print(f"Il numero {numeroDaCercare} è presente nella lista all'indice {listaNumeri.index(numeroDaCercare)}.")  # Se presente, stampa la posizione (indice) del numero nella lista
else:
    print(f"Il numero {numeroDaCercare} non è presente nella lista.")

    #NB. f string è una funzionalità di Python che permette di inserire variabili all'interno di stringhe
# il tutto senza mettere str o +

#ESERCIZIO MA SENZA LA FUNZIONE AUTOMATICA CE TROVA L'INDICE#

# if numeroDaCercare in listaNumeri:
#     for i in range(len(listaNumeri)): #len restituisce la lunghezza della lista
#         # Cicla attraverso gli indici della lista. 9

#         if listaNumeri[i] == numeroDaCercare:
#             print(f"Il numero {numeroDaCercare} è presente nella lista all'indice {i}.")
#             break
#     else:
#         print(f"Il numero {numeroDaCercare} non è presente nella lista.")
# Questo codice è un'alternativa che non utilizza il metodo index, ma cerca manualmente l'indice del numero.