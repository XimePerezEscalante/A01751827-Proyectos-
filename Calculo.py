import random

from random import randint

global a,b,c

#Función para generar las ecuaciones a derivar

def preguntas_deriv():

	complejidad = randint(1,3)

	ecuacion = []

	while complejidad > 0:
		a = randint(-9,9)

		b = ""

		c = randint(-9,9)

		while a == 0:

			a = randint(-9,9)

		

		if a == 1:

			ecuacion.append(("","x",c))

		elif c == 1:

			ecuacion.append(("","x",""))

		else:

			ecuacion.append((a,"x",c))

		
		
		complejidad = complejidad - 1


	"""a = randint(-9,9)

	b = ""

	c = randint(-9,9)

	while a == 0:

		a = randint(-9,9)

	ecuacion = []

	if a == 1:

		ecuacion.append(("","x",c))

	elif c == 1:

		ecuacion.append(("","x",""))

	else:

		ecuacion.append((a,"x",c))

	respuesta_deriv(a,b,c)"""

	return ecuacion

#Función para sacar las derivadas de las ecuaciones 

def respuesta_deriv(a,b,c,d):

	resultado = ""

	if c == 0:
		resultado = 0
    	#print(resultado)
    
	if a == 1:
		if c == 1:
			resultado = 1
		if c != 1:
			a1 = 1 * c
			c1 = c - 1
			res = [str(a1),str(b),"**",str(c1)]
			for i in res:
				resultado += i + ""

	if c != 1 and c != 0:
		
		a1 = a * c
		c1 = c - 1

		if signo_random == "-":

			a1 = a1 * -1

		res = [str(a1),str(b),"**",str(c1)]

		cont4 = 1

		for i in res:

			if cont4 > 1:

				if a1 > 0:

					resultado += "+" + i + "" 

			else: 

				resultado += i + "" 

		#resultado = (a1,b,"**",c1)

	if c == 1:
		resultado = a

	return str(resultado)


#Primero se muestra una introducción a cálculo junto con los temas disponibles

print("Cálculo Diferencial e Integral: Juega y aprende \n\nIntroducción \n\nCálculo es \
la matemática del cambio, de rectas tangentes, pendientes, áreas, volúmenes, \
longitudes de arcos, centroides, curvaturas, etc.\nA continuación se presentan \
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

        
        cont = 5
        cont2 = 0
        cont3 = 1
        puntos = 0
        lista = []
        signo = ["+","-"]
        signo_random = random.choice(signo)

        
        while cont > 0:

        	cont2 = cont2 + 1

        	print("Pregunta",cont2,":\nf(x) = ",end = "")

        	for n in preguntas_deriv():

        		if cont3 == 1:

        			print(n[0],n[1],"**",n[2],end = "")

        			cont3 = cont3 - 1

        		else:

        			print(signo_random,"(",n[0],n[1],"**",n[2],")",end = "")

        		if n == "":

        			n = 1

        		#if len(str(n[2])) == 0:

        			#n = 1

        	lista.extend((str(n[0]),str(n[1]),"**",str(n[2]),signo_random))

        		

        	#lista2 = ""
        	#for p in lista:
        		#lista2 += p + ""

        	#print(lista2)
        	respuesta = input("\nEscribe el resultado:\n")

        	if respuesta == respuesta_deriv(n[0],n[1],n[2],signo_random):
        		print("¡Correcto!     +2pts")
        		puntos = puntos + 2
        		print(puntos)

        	else:
        		print("¡Incorrecto!     +0pts")
        		puntos = puntos + 0
        		print(puntos)

        		print("RESULTADO:",respuesta_deriv(n[0],n[1],n[2],signo_random))
        	
        	cont = cont - 1
        	
        	print("cont =",cont)
            
        print("Puntos:",puntos)
        	

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
