# Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

listaNumeri = []  # Crea una lista vuota che conterrà i numeri inseriti dall'utente come stringhe
print("Inserisci i numeri da sommare (digita 'fine' per terminare):")  # Messaggio di istruzioni per l'utente
i = 0  # Inizializza una variabile per tenere traccia dell'indice corrente nella lista
somma = 0  # Inizializza la variabile che conterrà la somma totale

while True:  # Inizia un ciclo infinito che verrà interrotto solo con 'break'
    listaNumeri.append(input())  # Chiede all'utente un input e lo aggiunge alla lista (come stringa)
    if listaNumeri[i] == 'fine':  # Se l'ultimo elemento inserito è la stringa 'fine'
        break  # Esce dal ciclo
    else:
        somma += float(listaNumeri[i])  # Converte la stringa in numero (float) e la aggiunge alla somma
    i += 1  # Passa all'indice successivo

# Rimuoviamo l'ultimo elemento 'fine' dalla lista (FINE)
listaNumeri.pop()  # Elimina l'ultimo elemento della lista, che è la stringa 'fine'

print("La lista dei numeri inseriti è:", listaNumeri)  # Stampa la lista dei numeri inseriti (come stringhe)
print("La somma dei numeri inseriti è:", str(somma))  # Stampa la somma totale calcolata

# Nota: La somma è calcolata come float per gestire numeri decimali
# e la lista contiene gli input dell'utente come stringhe.

