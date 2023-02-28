import random


palabrasLista = ['Oposición', 'Naufragio', 'Tormentoso', 'Flotar', 'Terrible', 'Oveja', 'Erótica', 'Principiante', 'Granulado', 'Ubicuo', 'Describe', 'Libertad', 'Lista', 'Firme', 'Justificar', 'Gobierno', 'Empujar', 'Cable', 'Rol', 'Desconcertante', 'Tonto', 'Norte', 'Fáctico', 'Cut', 'Sentir', 'Algunos', 'Funeral', 'Verdugo', 'Zinc', 'Arrojar', 'Curvy', 'Gruñón', 'Destino', 'Digestión', 'Cashbox', 'Asombroso', 'Destino', 'Maldición', 'Temeroso']


def pickRandomWord():
    return palabrasLista[random.randint(0,len(palabrasLista)-1)]

def pasarList():
    palabras = ""
    palabraCurrent = ""
    palabrasLista.clear()
    palabras = input("Diccionario: ")
    for x in palabras:
        if(x == ","):
            palabrasLista.append(palabraCurrent)
            palabraCurrent = ""
        elif(x == " "):
            pass
        else:
            palabraCurrent += x
    return palabrasLista[random.randint(0,len(palabrasLista)-1)]