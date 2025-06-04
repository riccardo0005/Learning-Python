# Questa funzione prende una lista di numeri come input
# e stampa un istogramma usando asterischi.
# Per ogni numero nella lista, stampa una riga di asterischi
# lunga quanto il valore del numero.
# Esempio di utilizzo:
# lista = [3, 7, 9, 5]
# stampa_istogramma(lista)

def stampa_simbolo(lista):  # Definisce una funzione che riceve una lista di numeri
    for i in lista:  # Cicla su ogni numero nella lista
        print("*" * i)  # Stampa una riga di asterischi lunga quanto il numero
    print("Istogramma stampato con successo!")  # Messaggio di conferma

print("Quani numeri vuoi inserire?")  # Chiede all'utente quanti numeri vuole inserire
nNumeri = int(input())  # Legge il numero inserito e lo converte in intero

listaNumeri = [] * nNumeri  # (Non necessario: crea una lista vuota, la moltiplicazione non ha effetto)

for i in range(nNumeri):  # Cicla per il numero di volte richiesto dall'utente
    print(f"Inserisci il numero", i+1 , ":")  # Chiede di inserire il numero (la sintassi può essere migliorata)
    numero = int(input())  # Legge il numero inserito e lo converte in intero
    listaNumeri.append(numero)  # Aggiunge il numero alla lista

stampa_simbolo(listaNumeri)  # Chiama la funzione per stampare l'istogramma