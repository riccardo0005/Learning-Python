#CALCOLO DEL NUMERO MAGGIORE TRA DUE NUMERI#
print("INSERISCI DUE NUMERI:")
print("Il primo numero è: ", end="")
numeroUno = input()
print("Il secondo numero è: ", end="")
numeroDue = input()

if numeroUno < numeroDue:
    print("Il primo numero è minore del secondo")
elif numeroUno > numeroDue:
    print("Il primo numero è maggiore del secondo")
elif numeroUno == numeroDue:
    print("I due numeri sono uguali")
