"""

       
Funzione che converte una distanza espressa in metri nei corrispondenti valori in:
- miglia terrestri
- iarde
- piedi
- pollici

Argomenti:
    metri (float): valore della distanza in metri da convertire

Stampa:
    L'equivalente della distanza in:
    - miglia terrestri
    - iarde
    - piedi
    - pollici

Note:
    1 miglio terrestre = 1609.344 metri
    1 iarda = 0.9144 metri
    1 piede = 0.3048 metri
    1 pollice = 0.0254 metri
"""


def converti_distanza(metri):
    conversioni = {
        "Miglia terrestre": metri / 1609.344,
        "Iarde": metri / 0.9144,    
        "Piedi": metri / 0.3048, 
        "Pollici": metri / 0.0254
    }
    return conversioni

print("Conversione di una distanza espressa in metri nelle misure richieste. Inserisci misura in metri: ")
metri = float(input("Metri: "))

conversioni = converti_distanza(metri)
for misura, valore in conversioni.items():# # Itera su ciascuna coppia chiave-valore del dizionario 'conversioni', dove 'misura' è il nome dell'unità di misura e 'valore' è la distanza convertita.
    print(f"{misura}: {valore:.2f}")  # Stampa il valore convertito con due decimali


