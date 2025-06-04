# Scrivi una funzione che, data in ingresso una lista A contenente n parole,
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
#
# Questo esercizio può essere risolto anche usando una list comprehension.

#FUNZIONE INTERMEDIA NON TROPPO EFFICENTE#
def lunghezza_parole(A):  # Definisce una funzione che prende una lista di parole come parametro
    B = []  # Crea una lista vuota che conterrà le lunghezze delle parole
    for parola in A:  # Cicla su ogni parola nella lista A
        B.append(len(parola))   # Calcola la lunghezza della parola e la aggiunge alla lista B
    return B  # Restituisce la lista delle lunghezze

#FUNZIONE EFFICENTE OTTIMIZZATA CON #
def lunghezza_parole(A):  # Definisce una funzione che prende una lista di parole come parametro
    return [len(parola) for parola in A]  # Usa una list comprehension per creare una lista delle lunghezze delle parole
#NB. questa len comprehension prima chiede l'operazione di len su ogni parola in A e poi il ciclo sul quale si basa per creare la lista B
#NB2. si usano le parentesi quadre perchè stiamo creando una lista B che ci verrà restituita e poi sparirà#
print("Quanti elementi vuoi inserire nella lista A?")  # Chiede all'utente quanti elementi vuole inserire
n = int(input())    # Legge il numero inserito e lo converte in intero
A = [] * n  # (Non necessario: crea solo una lista vuota, la moltiplicazione non ha effetto)
for i in range(n):  # Cicla n volte per inserire n parole
    print("Inserisci la parola numero", i + 1, ":")  # Chiede di inserire la parola numero i+1
    A.append(input())  # Aggiunge la parola inserita alla lista A

print(f"La lista A ha le parole rispettivamente di lunghezza:", lunghezza_parole(A))  # Stampa la lista delle lunghezze delle parole

#NB3. in entrambi i casi la lista non esiste fuori dalla funzione perchè non labbiamo assegnata ad una variabile tipo cosi:
# risultato = lunghezza_parole(parametro)#