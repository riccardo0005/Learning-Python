#TROVA IL MAGGIORE TRA TRE NUMERI OTTIMIZZATO SENZA FUNZIONE AUTOMATICA#
print("Inserisci tre numeri:")
nUno = input("Primo numero: ")
nDue = input("Secondo numero: ")
nTre = input("Terzo numero: ")
print("I numeri inseriti sono:", nUno, nDue, nTre)
i = 1

if nUno == nDue or nUno == nTre or nDue == nTre:
        print("Attenzione, hai inserito due numeri uguali!")
else:
    if nUno > nDue and nUno > nTre:
        max = nUno
    elif nDue > nUno and nDue > nTre:
        max = nDue
    elif nTre > nUno and nTre > nDue:
        max = nTre
    
    print("Il numero maggiore è:", max)