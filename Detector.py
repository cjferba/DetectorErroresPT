# -*- coding: cp1252 -*-
STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_VIO  = 0x05
FOREGROUND_AMA  = 0x06
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

import ctypes
import random

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_color(color, handle=std_out_handle):
    """(color) -> BOOL
    
    Example: set_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
    """
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

def sumax(lis):
    cont=0
    for i in range(len(lis)):
        cont=int(lis[i])+cont
        
    if cont%2==0:
        return True
    else:
        return False

#**###############MAIN###############**#

#entrada de datos
codificacion = {"a":"00000", "b":"00001", "c":"00010", "d":"00011", "e":"00100", "f":"00101",
                "g":"00110", "h":"00111", "i":"01000", "j":"01001", "k":"01010", "l":"01011",
                "m":"01100", "n":"01101", "o":"01110", "p":"01111", "q":"10000", "r":"10001",
                "s":"10010", "t":"10011", "u":"10100", "v":"10101", "w":"10110", "x":"10111",
                "y":"11000", "z":"11001", ".":"11010", ",":"11011", " ":"11100", ";":"11101", ":":"11110", "?":"11111"}
codificacion.update( dict((codificacion[k], k) for k in codificacion))
color= (FOREGROUND_GREEN,FOREGROUND_BLUE,FOREGROUND_RED,FOREGROUND_VIO,FOREGROUND_AMA)
salida1=[]
salida2=[]
alfa=int(raw_input("Introducir Alfa...\n"))
while (alfa>0) and (alfa>=100):
    alfabeto=int(raw_input("Introducir Alfa...\n"))
entrada=raw_input("Introducir secuencia...\n")
for i in range(len(entrada)):
    salida1.append(str(codificacion[entrada[i]]))
#Añadimos el bits horizontal para ver errores
for i in range(len(salida1)):
    cont=0
    for u in range(len(salida1[i])):
        cont=(int(salida1[i][u])+cont) % 2
    salida1[i]=salida1[i]+str(cont)
#ERRORES que le insertamos(RUIDO)
x=""
for i in range(len(salida1)):
    #print salida1[i]
    for u in range(len(salida1[i])):
        a=random.randint(1,100)
        #print "a es: ",a,"x es:",x
        if a<=alfa:
            if salida1[i][u]=='0':
                x=x+"1"
            else:
                x=x+"0"
        else:
            x=x+salida1[i][u]
    salida2.append(x)
    x=''
print "\nOriginal:",
for i in range(len(salida1)):
    print "[",
    for u in range(len(salida1[i])):
        print salida1[i][u],
    print "]",
print "\nLLegada :",

for i in range(len(salida1)):
    set_color(0x07)
    print "[",
    for u in range(len(salida1[i])):
        if salida1[i][u]<>salida2[i][u]:
            set_color(color[2])
            print salida2[i][u],
        else:
            set_color(color[0])
            print salida2[i][u],
    set_color(0x07)
    print "]",

print "\nEnviado:"
print entrada
print "Decodificado:"
decodificacion=[]
#decodificacion
for i in range(len(salida2)):
    if sumax(salida2[i][:]):
        decodificacion.append(str(codificacion[salida2[i][0:5]]))
    else:
        decodificacion.append("error")
for i in range(len(decodificacion)):
    if decodificacion[i]=="error":
        set_color(color[2])
        print "E",
    else:
        set_color(color[0])
        print decodificacion[i],
set_color(0x07) 
raw_input("")
