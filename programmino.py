print("inserisci quanti numeri vuoi")
somma = 0
w= 0
while w==0 :
    numero = int(input("Inserisci un numero intero (0 per terminare): "))
    if numero!= 0:
        somma += numero
    else:
        w=1
print("la somma dei numeri inseriti è:", somma)
