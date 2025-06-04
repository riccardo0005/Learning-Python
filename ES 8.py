# Questa funzione restituisce la lunghezza di una stringa o lista passata
# come parametro.
# È una versione personalizzata della funzione incorporata len di Python.

def lunghezzaElemento(elemento):  # Definisce una funzione che riceve una stringa o una lista
    cont = 0  # Inizializza un contatore a zero
    for i in elemento:  # Cicla su ogni elemento della stringa o lista
        if i in elemento:  # (Questa condizione è sempre vera, quindi non è necessaria)
            cont += 1  # Incrementa il contatore per ogni elemento
    return cont  # Restituisce il conteggio degli elementi

def FunzioneIntegrata(elemento):  # Definisce una funzione che riceve una stringa o una lista
    return len(elemento)  # Restituisce la lunghezza dell'elemento usando la funzione incorporata len

print("Inserisci una stringa o una lista:")  # Messaggio introduttivo

print("Scrivi stringa:")  # Chiede all'utente di inserire una stringa
elementoUno = input()  # Legge la stringa inserita dall'utente

print("Scrivi lista di 4 elementi:")  # Chiede di inserire una lista di 4 elementi
elementoDue = [] * 4  # (Non necessario: crea solo una lista vuota)

for i in range(4):  # Cicla 4 volte per inserire 4 elementi nella lista
    print("Elemento ", i + 1, " ")  # Chiede di inserire l'elemento i+1
    elementoDue.append(input())  # Aggiunge l'elemento inserito alla lista

print("Elementi della lista: ", elementoDue)  # Stampa la lista inserita dall'utente
print("Lunghezza della lista: ", lunghezzaElemento(elementoDue))  # Stampa la lunghezza della lista usando la funzione personalizzata

print("Elementi della stringa: ", elementoUno)  # Stampa la stringa inserita dall'utente
print("Lunghezza della stringa: ", lunghezzaElemento(elementoUno))  # Stampa la lunghezza della stringa usando la funzione personalizzata

# La funzione lunghezzaElemento conta gli elementi in una stringa o lista