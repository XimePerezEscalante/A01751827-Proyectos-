#Bibliotecas
import random
from random import randint

global a,b,c

def func_signo():

	#Devuelve el signo utilizando la biblioteca random, si la ecuación tiene más de un elemento.

	signo = ["+","-"]
	signo_random = random.choice(signo)
	return signo_random


def preguntas_deriv():

	"""
	Devuelve la ecuación a derivar, de la complejidad dependerá el número de elementos a derivar.
	a: coeficiente
	b: literal
	c: exponente
	"""

	complejidad = randint(1,3)
	ecuacion = []
	lista_exp = []
	lista_coef = []

	while complejidad > 0:

		a = randint(-9,9)
		b = ""
		c = randint(-9,9)

		while a == 0:
			a = randint(-9,9)

		while a == 1:
			a = randint(-9,9)

		while c == 1:
			c = randint(-9,9)

		ecuacion.append((a,"x",c))
		complejidad = complejidad - 1

	return ecuacion



def respuesta_deriv(e,lista_signo):

	"""
	Recibe el coeficiente y el exponente de cada elemento de la ecuación a derivar.
	Deriva la ecuación, multiplica el coeficiente y el exponente, después le resta
	1 al exponente, si el signo de la función func_signo es negativo, multiplica el 
	coeficiente por -1. Si el exponente, el coeficiente o ambos son igual a 1, no los 
	muestra.
	Devuelve el resultado completo de la ecuación.
	 """

	cont = 0
	res = []
	num = 0
	cont2 = 0
	cont3 = 0
	resultado = ""

	while cont <= len(e):

		for i in e:

			cont = cont + 1

			while num < len(e):

				exp = e[num][1]
				coef = e[num][0]

				if exp == 0:

					if cont3 == 0 and len(e) == 1:
						res.append("0")

				elif exp == 1:

					if len(e) > 1:

						if cont3 == 1:
							signo2 = lista_signo[0]

							if signo2 == "-":
								coef = coef * -1


						elif cont3 == 2:
							signo2 = lista_signo[1]

							if signo2 == "-":
								coef = coef * -1

					else:
						res.append(str(coef))

				else:

					exp = e[num][1] - 1
					coef = e[num][0] * e[num][1]

					if len(e) > 1:

						if cont3 == 1:
							signo2 = lista_signo[0]

							if signo2 == "-":
								coef = coef * -1


						elif cont3 == 2:
							signo2 = lista_signo[1]

							if signo2 == "-":
								coef = coef * -1


					if cont2 > 0:

						if coef > 0:

							if exp == 1:
								res.append(("+",str(coef),"x"))

							else:
								res.append(("+",str(coef),"x^",str(exp)))

						else:

							if exp == 1:
								res.append((str(coef),"x"))

							else:
								res.append((str(coef),"x^",str(exp)))

					else:

						if exp == 1:
							res.append((str(coef),"x"))

						else:
							res.append((str(coef),"x^",str(exp)))

					cont2 = cont2 + 1		

				num = num + 1
				cont3 = cont3 + 1

	if len(res) > 0:

		for x in res:
				for g in x:
					resultado += g + "" 

	return str(resultado)

def trigonometricas():

	#Escoge una función trigonométrica a derivar.

	lista_trig_deriv = ["sen","cos","tan","sec","cot","csc"]
	opcion_trig = random.choice(lista_trig_deriv)
	return opcion_trig

def preguntas_deriv_trig():

	"""Regresa la ecuación a derivar.
	a: coeficiente
	b: literal
	c: exponente
	"""

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

def respuesta_deriv_trig(d,a,b,c):

	"""
	Función que resuelve la derivada, en el diccionario viene la derivada de cada función; multiplica el exponente 
	con el coeficiente y a este último le resta 1. Si la función que recibe es coseno, cotangente o cosecante, al 
	coeficiente se le multiplica por -1.
	"""

	resultado = ""
	res = []
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

			else:
				res = [str(a1),str(b),"^",str(c1),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

		elif d == "csc":
			a1 = a1 * -1

			if c1 == 1:
				res = [str(a1),str(b),"csc(",str(a),str(b),"^",str(c),")cot(",str(a),str(b),"^",str(c),")"]

			else:
				res = [str(a1),str(b),"^",str(c1),"csc(",str(a),str(b),"^",str(c),")cot(",str(a),str(b),"^",str(c),")"]

		elif d == "sec":

			if c1 == 1:
				res = [str(a1),str(b),"sec(",str(a),str(b),"^",str(c),")tan(",str(a),str(b),"^",str(c),")"]
			
			else:
				res = [str(a1),str(b),"^",str(c1),"sec(",str(a),str(b),"^",str(c),")tan(",str(a),str(b),"^",str(c),")"]

		else:

			if c1 == 1:
				res = [str(a1),str(b),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

			else:
				res = [str(a1),str(b),"^",str(c1),deriv_trig[d],"(",str(a),str(b),"^",str(c),")"]

		for i in res:

			resultado += i + "" 

	return str(resultado)

def calif(puntos):

	#Función para mostrar diferentes mensajes dependiendo el puntaje que haya obtenido el usuario.

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



def juego_deriv():

	"""
	Función para generar cada ronda de 5 preguntas, recibe la ecuación de la función preguntas_deriv,
	el signo de func_signo y los manda a respuesta_deriv, si la respuesta del usuario es igual a la
	respuesta de la función, se le suman dos puntos y al final se manda llamar a la función calif que 
	recibe los mismos como parámetro.
	"""

	cont2 = 0
	puntos = 0
	signo_final = ""


	while cont2 < 5:

		cont2 = cont2 + 1
		cont3 = 1
		lista_signo = []
		lista = []

		print("--------------------------------\nPregunta",cont2,":\n\nf(x) = ",end = "")

		for n in preguntas_deriv():

			if cont3 == 1:
				print(n[0],n[1],"^",n[2],end = " ")
				lista.append([n[0],n[2]])
				cont3 = cont3 + 1

			else:
				signo_final = func_signo()
				print(" ",signo_final,"(",n[0],n[1],"^",n[2],")",end = "")
				lista.append([n[0],n[2]])

			if n == "":
				n = 1
			lista_signo.append(signo_final) 

			if len(lista_signo) == len(lista):
				lista_signo.pop(0)			

		respuesta = input("\n\nf'(x) = ")

		if respuesta == respuesta_deriv(lista,lista_signo):
			print("\n¡Correcto!     +2pts\n")
			puntos = puntos + 2
			

		else:
			print("\n¡Incorrecto!     +0pts")
			puntos = puntos + 0
			print("RESULTADO:",respuesta_deriv(lista,lista_signo),"\n")

	print("--------------------------------\nPuntos:",puntos,"\n")

	calif(puntos)

def juego_trig():

	"""
	Función para generar cada ronda de 5 preguntas, recibe la ecuación de la función preguntas_deriv,
	el signo de func_signo y los manda a respuesta_deriv, si la respuesta del usuario es igual a la
	respuesta de la función, se le suman dos puntos y al final se manda llamar a la función calif que 
	recibe los mismos como parámetro.
	"""

	cont2 = 0
	puntos = 0

	while cont2 < 5:

		cont2 = cont2 + 1
		print("--------------------------------\nPregunta",cont2,":\nf(x) = ",end = "")

		for n in preguntas_deriv_trig():
			print(n[0],"(",n[1],n[2],"^",n[3],")")

		respuesta = input("\nf'(x) = ")

		if respuesta == respuesta_deriv_trig(n[0],n[1],n[2],n[3]):
			print("\n¡Correcto!     +2pts")
			puntos = puntos + 2

		else:
			print("\n¡Incorrecto!     +0pts")
			puntos = puntos + 0
			print("RESULTADO:",respuesta_deriv_trig(n[0],n[1],n[2],n[3]))
	 
	print("--------------------------------\nPuntos:",puntos,"\n")
	calif(puntos)

print("""
		   Cálculo Diferencial: Juega y aprende

INTRODUCCIÓN

Cálculo es la matemática del cambio, de rectas tangentes, pendientes, áreas, vo-
lúmenes, longitudes de arcos, centroides, curvaturas, etc.

DERIVACIÓN

Así se le conoce al proceso de hallar la derivada de una función. Una función es
diferenciable en x si su derivada existe en x, y es diferenciable sobre un in-
tervalo abierto (a,b), si es diferenciable en todos los puntos en el intervalo. 
Sus notaciones más comunes son:

		    	f'(x), dy/dx, y', Dx[y]

Nosotros usaremos f'(x). 

Deberás recordar que:

		1. La derivada de una constante es igual a 0:

				  f’(5) = 0

		2. La derivada de una variable es igual a 1:

				  f’(x) = 1

A continuación, te mostraremos cómo derivar la ecuación F(x) = x^n
Donde n representa al exponente y el coeficiente es igual a 1.
Porque recordemos que todo está multiplicado, dividido y elevado a la 1.

¡Empecemos!

Lo primero que debes hacer es multiplicar el exponente n por el coeficiente:

	n * 1 = n

Por lo que ahora tenemos que:

	f’(x) = nx^n

Después debes restarle 1 al exponente.

Por lo tanto:

	f’(x) = nx^n-1

Ahora veamos un ejemplo:

	F(x) = 3x^2

	f’(x) = 6x

Bien, si la ecuación tiene más de un elemento, deberás derivarlos uno por uno. 
Como se muestra a continuación:

	F(x) = 6x^3 - 4x^2 + 5x + 7

	f’(x) = 18x^2 -8x + 5

		""")

practicar = input("\nDeseas practicar este tema?\n\nS = Sí\n\nN = No\n")

if practicar == "n" or practicar == "N":

	print("""¡No hay problema!
Aquí hay más ejemplos:

	F(x) = 10x^-2

	f’(x) = -20x^-3
-----------------------
	F(x) = 9x

	f'(x) = 9
-----------------------

	F(x) = 8x^4 - 5x

	f'(x) = 32x^3 - 5
-----------------------
""")

practicar = input("\nDeseas practicar o pasar al siguiente tema?\n\nS = Practicar\n\nN = Siguiente tema\n")

while practicar == "S" or practicar == "s":

	juego_deriv()
	practicar = input("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n")

	if practicar == "n" or practicar == "N":
		practicar = input("¿Estás segur@?\n\nS = Sí\n\nN = No\n")

		if practicar == "s" or practicar == "S":
			practicar = "n"
 
#Cuando el usuario decide dejar de practicar este tipo de derivadas, se pasa al tema de funciones trigonométricas que están en otro archivo.

print("¡De acuerdo!\n--------------------------------\n\nA continuación aprenderás a derivar funciones trigonométricas")
print("""
f’(senx) = cosx
f’(cosx) = -senx
f’(tanx) = sec ^ 2 x
f’(cotx) = -csc ^ 2 x
f’(secx) = tanx secx
f’(cscx) = -cotx cscx""")

practicar = input("¿Deseas practicar este tema?\n\nS = Sí\n\nN = No\n")

while practicar == "S" or practicar == "s":
	juego_trig()
	practicar = input("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n")

	if practicar == "n" or practicar == "N":
		practicar = input("¿Estás segur@?\n\nS = Sí\n\nN = No\n")

		if practicar == "s" or practicar == "S":
			practicar = "n"

print("¡De acuerdo!\n--------------------------------")
