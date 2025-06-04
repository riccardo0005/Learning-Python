# Questa funzione prende una stringa come parametro e restituisce un dizionario
# che rappresenta la frequenza di comparsa di ciascun carattere nella stringa.
# Ad esempio, per la stringa "ababcc", il risultato sarà {"a": 2, "b": 2, "c": 2}.


# Definizione della funzione che prende una stringa come parametro
def dizionario(stringa):
    dizionario = {}  # Inizializza un dizionario vuoto per memorizzare le frequenze
    for carattere in stringa:  # Itera su ogni carattere della stringa
        if carattere in dizionario:  # Se il carattere è già presente nel dizionario
            dizionario[carattere] += 1  # Incrementa il conteggio di 1
        else:
            dizionario[carattere] = 1  # Altrimenti, aggiungi il carattere con valore 1
    return(dizionario)  # Stampa il dizionario risultante
            
print("Inserisci una stringa:")  # Chiede all'utente di inserire una stringa
elemento = input()  # Legge la stringa inserita dall'utente
print(dizionario(elemento))  # Chiama la funzione passando la stringa inserita

print(dizionario(elemento).keys())  # Stampa le chiavi del dizionario
print(dizionario(elemento).values())  # Stampa i valori del dizionario