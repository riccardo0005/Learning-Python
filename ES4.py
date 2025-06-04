# Scrivi un programma che chieda all'utente una stringa composta da un 
# solo carattere e dica se si tratta di una vocale oppure no.

# ESERCIZIO CON LA LISTA #
car = input("Inserisci un carattere: ")  # Chiede all'utente di inserire un carattere
listaVocali = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']  # Lista di tutte le vocali (maiuscole e minuscole)
if car in listaVocali:  # Controlla se il carattere inserito è una vocale
    print("Il carattere inserito è una vocale.")  # Stampa se è una vocale
else:
    print("Il carattere inserito non è una vocale.")  # Stampa se non è una vocale

# ESERCIZIO CON IL CICLO FOR #
car = input("Inserisci un carattere: ")  # Chiede nuovamente un carattere all'utente
vocali = "aeiouAEIOU"  # Stringa contenente tutte le vocali (maiuscole e minuscole)
is_vocale = False  # Inizializza una variabile booleana per verificare se è una vocale
for v in vocali:  # Cicla su ogni vocale nella stringa
    if car == v:  # Se il carattere inserito corrisponde a una vocale
        is_vocale = True  # Imposta la variabile a True
        break  # Esce dal ciclo perché ha trovato una corrispondenza
if is_vocale:  # Se la variabile è True
    print("Il carattere inserito è una vocale.")  # Stampa se è una vocale      
else:
    print("Il carattere inserito non è una vocale.")    # Stampa se non è una vocale
# ESERCIZIO IN MODO LINEARE PER PRINCIPIANTI#
car = input("Inserisci un carattere: ")  # Chiede all'utente di inserire un carattere
if car == 'a' or car == 'e' or car == 'i' or car == 'o' or car == 'u' or \
   car == 'A' or car == 'E' or car == 'I' or car == 'O' or car == 'U':  # Controlla se il carattere è una vocale
    print("Il carattere inserito è una vocale.")  # Stampa se è una vocale
else:
    print("Il carattere inserito non è una vocale.")
