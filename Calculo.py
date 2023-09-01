import random

from random import randint

global a,b,c

#Función para generar las ecuaciones a derivar

def preguntas_deriv():


	a = randint(1,9)

	coeficiente = [True,False]

	coef = random.choice(coeficiente)

	if coef == True:
		coef = "x"
		b = 1
	else:
		coef = ""
		b = 0

	c = randint(0,9)

	ecuacion = []

	ecuacion.append((a,coef,c))

	return ecuacion

#Función para sacar las derivadas de las ecuaciones 

def respuesta_deriv(a,b,c):

	if len(str(b)) == 0:
		b = 0

	resultado = ""

	if c == 0:
		resultado = 0

	if b == 0:
		resultado = 0
		

	if c != 1 and c != 0 and b != 0:
		
		a1 = a * c
		c1 = c - 1
		resultado = (a1,b,"**",c1)

	if c == 1:
		resultado = a
	
	return str(resultado)


#Primero se muestra una introducción a cálculo junto con los temas disponibles

print("Cálculo Diferencial e Integral: Juega y aprende \n\nIntroducción \n\nCálculo es \
la matemática del cambio, de rectas tangentes, pendientes, áreas, volúmenes, \
longitudes de arcos, centroides, curvaturas, etc.\nA continuación se presentan\
los temas que se abordarán en este libro:\n1. Derivación\n2. Integración")

"""Después de que el usuario escoge el tema se le mostrará la explicación y
después se le preguntará si desea practicar"""

tema = int(input("Escoge el tema que te gustaría aprender (Escribe 1 o 2):\n"))

while tema!=1 and tema!=2:
    tema = int(input("Escoge el tema que te gustaría aprender (Escribe 1 o 2):\n"))

if tema == 1:
    print("Derivación\n\nLa derivación se define como...\n")
    practicar = input("Deseas practicar este tema?\n\nPresiona la tecla S para practicar o la tecla N si deseas seguir leyendo o pasar a otro tema:\n")
    if practicar == "S" or practicar == "s":

        print("¡Empecemos!\nPregunta 1:\n")

        for n in preguntas_deriv():
			
          print("f(x) = ",n[0],n[1],"**",n[2])
	

        respuesta = input("Escribe el resultado:\n")
      
#Todavía tengo que corregir la comparación de respuestas cuando el resultado es diferente de 0
        
        if respuesta == respuesta_deriv(n[0],n[1],n[2]):
            print("¡Correcto!     +2pts")
            puntos = 2
        else:
        	print("¡Incorrecto!   +0pts")
        	puntos = 0

    elif practicar == "N" or practicar == "n":
    
        print("¡De acuerdo! Toma el tiempo que necesites hasta que te sientas list@ para practicar.")

elif tema == 2:
    print("Integración\n\nLa integración se define como...\n")
    practicar = input("Deseas practicar este tema?\n\nPresiona la tecla S para practicar o la tecla N si deseas seguir leyendo o pasar a otro tema:\n")
    if practicar == "S" or practicar == "s":
            respuesta = int(input("Cada ronda tendrá 5 preguntas y cada una valdrá 2 puntos. Este es un ejemplo, escribe 1 para seguir.\n"))
            
            if respuesta == 1:
                puntos = 2
                print("¡Correcto!   +2pts")
            else:
                print("¡Incorrecto!   +0pts")
                puntos = 0
            
                
            """Al final el usuario puede ver cuántos puntos tiene en total"""
            
            print("Puntos = ",puntos)
            
    elif practicar == "N" or practicar == "n":
    
        print("¡De acuerdo! Toma el tiempo que necesites hasta que te sientas list@ para practicar.")
