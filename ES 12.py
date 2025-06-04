# Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti,
# passati dall'utente tramite funzione input, in secondi.

def converti_in_secondi(contNumeri):

    giorni = (contNumeri[0]) * 86400  # 1 giorno = 86400 secondi
    ore = (contNumeri[1]) * 3600       # 1 ora = 3600 secondi
    minuti = (contNumeri[2]) * 60       # 1 minuto = 60 secondi
    return giorni + ore + minuti    


print("Inserisci giorni, ore e minuti separati da spazi.")


# Chiede all'utente di inserire i valori per giorni, ore e minuti
input_value = input("Inserisci il valore (giorni, ore, minuti): ")

contNumeri = [int(n) for n in input_value.split()]  # input_value.split() Divide l'input in una lista di stringhe per cui noi usiamo questa
# list comprehension per convertire in interi con int(n) e creare una lista di interi.
a = converti_in_secondi(contNumeri)  # Chiama la funzione per convertire in secondi


print(f"I valori inseriti corrispondono a:  {a} secondi.")  # Stampa il risultato della conversione
# Nota: La funzione converti_in_secondi accetta una lista di stringhe, quindi è necessario convertire i valori in interi.   
