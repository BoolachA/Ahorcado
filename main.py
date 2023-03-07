import os
import main
import diccionario

historial = ""
palabra = ""
numeroLetras = 0
ultimaLinea = ""
intento = ""
vidas = 4

print("1 - Poner un diccionário\n2 - Usar diccionário default\n3 - Escribir palabra\n")
opcion = int(input("Opc: "))
os.system("cls")
match opcion:
    case 1:
        palabra = diccionario.pasarList().upper()
    case 2:
        palabra = diccionario.pickRandomWord().upper()
    case 3:
        palabra = input("Escriba una palabra: ").upper()

palabra = palabra.replace("Ó", "O").replace("Á", "A").replace("É","E").replace("Í","I").replace("Ú","U")


numeroLetras = len(palabra)
ultimaLinea = "|     " + "_ " * numeroLetras

os.system("cls")

def gameOver():
    os.system("cls")
    print("G A M E    O V E R\nLa palabra era: "+main.palabra)
    os.system("pause")
    exit()

def gameFinish():
    os.system("cls")
    print("HAS ADIVINADO LA PALABRA!\nLa palabra era: "+main.palabra)
    os.system("pause")
    exit()

def actualizaLinea(numeroLetras):
    os.system("cls")
    print(numeroLetras)
    lastPos=0
    while(numeroLetras!=0):
        pos = 6 + 2 * palabra.find(intento,lastPos)
        lastPos=palabra.find(intento,lastPos)+1
        main.ultimaLinea=ultimaLinea[:pos]+intento+ultimaLinea[pos+1:]
        numeroLetras=numeroLetras-1
    constructor("Letra aceptada")

def constructor(feedback):
    if(ultimaLinea.find("_")==-1):
        gameFinish()
    os.system("cls")
    print("Vidas: ", main.vidas)
    match main.vidas:
        case 4:
            print("|---------------|\n|               |\n|\n|\n|\n|\n|")
        case 3:
            print("|---------------|\n|               |\n|               0\n|\n|\n|\n|")
        case 2:
            print("|---------------|\n|               |\n|               0\n|              \|/\n|\n|\n|")
        case 1:
            print("|---------------|\n|               |\n|               0\n|              \|/\n|               |\n|\n|")
        case 0:
            print("|---------------|\n|               |\n|               0\n|              \|/\n|               |\n|              / \ \n|")
            gameOver()
    print(ultimaLinea)
    print(feedback)


constructor("Prueba una letra")

#if __name__ == "__main__":
while (True):
    intento = input("Letra: ").upper()
    if(len(intento)>1):
        constructor("Porfavor digite solamente una letra")
    else:
        if (historial.find(intento) != -1):
            constructor("Letra no disponible")
        else:
            historial = historial + intento
            if (palabra.find(intento) != -1):
                numeroLetras=palabra.count(intento)
                actualizaLinea(numeroLetras)
            else:
                main.vidas = main.vidas - 1
                constructor("Letra incorrecta")