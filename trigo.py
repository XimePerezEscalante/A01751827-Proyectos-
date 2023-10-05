import random

from random import randint

from getkey import getkey, keys

global a,b,c,derivadaTrig,intTrig

#Escoge una función trigonométrica a derivar.

def trigonometricas():

	lista_trig_deriv = ["sen","cos","tan","sec","cot","csc"]

	opcion_trig = random.choice(lista_trig_deriv)

	return opcion_trig

#Escoge una función trigonométrica a integrar, en proceso.

def trig_int():

	lista_trig_int = ["sen","cos","sec**2","sectan","csc**2","csccot"]

	opcion_int = random.choice(lista_trig_int)

	return opcion_int

"""Regresa la ecuación a integrar, en proceso.
a: coeficiente
b: literal
c: exponente
"""

def preguntas_deriv_int():

	ecuacion = []

	intTrig = trig_int()

	a = randint(-9,9)

	b = ""

	c = randint(-9,9)

	if intTrig == "sectan":

		ecuacion.append(("sec(",a,"x",c,")tan(",a,"x",c,")"))

		ecuacion.append((a,"x",c))

	elif intTrig == "csccot":

		ecuacion.append(("csc(",a,"x",c,")cot(",a,"x",c,")"))

	else:

		ecuacion.append((intTrig,a,"x",c))

"""Regresa la ecuación a derivar.
a: coeficiente
b: literal
c: exponente
"""

def preguntas_deriv_trig():

	ecuacion = []

	derivadaTrig = trigonometricas()

	a = randint(-9,9)

	b = ""

	c = randint(-9,9)

	while a == 0 or a == 1:

		a = randint(-9,9)

	while c == 1:

		c = randint(-9,9)

	ecuacion.append((derivadaTrig,a,"x",c))

	return ecuacion

"""
Función que resuelve la derivada, en el diccionario viene la derivada de cada función; multiplica el exponente 
con el coeficiente y a este último le resta 1. Si la función que recibe es coseno, cotangente o cosecante, al 
coeficiente se le multiplica por -1.
"""

def respuesta_deriv_trig(d,a,b,c):

	resultado = ""

	res = []

	#deriv_trig = {"sen":"cos","cos":"sen","tan":"sec**2","cot":"csc**2","sec":"sec(x)tan(x)","csc":"csc(x)cot(x)"}
	deriv_trig = {"sen":"cos","cos":"sen","tan":"sec^2","cot":"csc^2","sec":"sec(x)tan(x)","csc":"csc(x)cot(x)"}

	if c == 0:

		resultado = 0

	if c != 1 and c != 0:
		
		a1 = a * c
		c1 = c - 1

		if d == "cos" or d == "cot":

			a1 = a1 * -1

			if c1 == 1:

				res = [str(a1),str(b),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

			#res = [str(a1),str(b),"**",str(c1),deriv_trig[d],"(",str(a),str(b),"**",str(c),")"]

			else:

				res = [str(a1),str(b),"^",str(c1),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

		elif d == "csc":

			a1 = a1 * -1

			if c1 == 1:

				res = [str(a1),str(b),"csc(",str(a),str(b),"^",str(c),")cot(",str(a),str(b),"^",str(c),")"]

			#res = [str(a1),str(b),"**",str(c1),"csc(",str(a),str(b),"**",str(c),")cot(",str(a),str(b),"**",str(c),")"]

			else:

				res = [str(a1),str(b),"^",str(c1),"csc(",str(a),str(b),"^",str(c),")cot(",str(a),str(b),"^",str(c),")"]

		elif d == "sec":

			if c1 == 1:

				res = [str(a1),str(b),"sec(",str(a),str(b),"^",str(c),")tan(",str(a),str(b),"^",str(c),")"]

			#res = [str(a1),str(b),"**",str(c1),"sec(",str(a),str(b),"**",str(c),")tan(",str(a),str(b),"**",str(c),")"]
			
			else:

				res = [str(a1),str(b),"^",str(c1),"sec(",str(a),str(b),"^",str(c),")tan(",str(a),str(b),"^",str(c),")"]

		else:

			if c1 == 1:

				res = [str(a1),str(b),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

			#res = [str(a1),str(b),"**",str(c1),deriv_trig[d],"(",str(a),str(b),"**",str(c),")"]

			else:

				res = [str(a1),str(b),"^",str(c1),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

		for i in res:

			resultado += i + "" 

	return str(resultado)

#Función para mostrar diferentes mensajes dependiendo el puntaje que haya obtenido el usuario.

def calif(puntos):

	if puntos == 10: 

		print("¡Excelente!\n--------------------------------")

	elif puntos == 8:

		print("¡Increíble!\n--------------------------------")

	elif puntos == 6:

		print("¡Muy bien!\n--------------------------------")

	elif puntos == 4:

		print("¡Tú puedes!\n--------------------------------")

	elif puntos == 2:

		print("¡No te rindas!\n--------------------------------")

	else:

		print("¡No pasa nada, la práctica hace al maestro!\n--------------------------------")

"""
Función para generar cada ronda de 5 preguntas, recibe la ecuación de la función preguntas_deriv,
el signo de func_signo y los manda a respuesta_deriv, si la respuesta del usuario es igual a la
respuesta de la función, se le suman dos puntos y al final se manda llamar a la función calif que 
recibe los mismos como parámetro.
"""

def juego_trig():

	#cont = 5
	cont2 = 0
	puntos = 0

	while cont2 < 5:

		cont2 = cont2 + 1

		print("--------------------------------\nPregunta",cont2,":\nf(x) = ",end = "")

		for n in preguntas_deriv_trig():

			#print(n[0],"(",n[1],n[2],"**",n[3],")")
			print(n[0],"(",n[1],n[2],"^",n[3],")")



		respuesta = input("\nf'(x) = ")

		if respuesta == respuesta_deriv_trig(n[0],n[1],n[2],n[3]):
			print("\n¡Correcto!     +2pts")
			puntos = puntos + 2

		else:
			print("\n¡Incorrecto!     +0pts")
			puntos = puntos + 0
			print("RESULTADO:",respuesta_deriv_trig(n[0],n[1],n[2],n[3]))
		
		#cont = cont - 1
	
    
	print("--------------------------------\nPuntos:",puntos,"\n")

	calif(puntos)


print("¿Deseas practicar este tema?\n\nS = Sí\n\nN = No\n")

key = getkey()

while key == "s" or key == "S":

	juego_trig()

	print("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n")

	key = getkey()

	if key == "n" or key == "N":

		print("¿Estás segur@?\n\nS = Sí\n\nN = No\n")

		key = getkey()

		if key == "s" or key == "S":

			key = "n"

print("¡De acuerdo!\n--------------------------------")







