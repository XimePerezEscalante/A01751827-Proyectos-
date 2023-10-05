import random

from random import randint

from getkey import getkey, keys

global a,b,c

#Función para definir el signo si la pregunta es una suma de derivadas.

def func_signo():

	signo = ["+","-"]

	signo_random = random.choice(signo)

	return signo_random

"""
Función que regresa la ecuación a derivar, de la complejidad dependerá el número de elementos a derivar.
a: coeficiente
b: literal
c: exponente
"""

def preguntas_deriv():

	complejidad = randint(1,3)

	ecuacion = []

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

"""
Función que deriva la ecuación, sólo recibe el coeficiente y el exponente para multiplicarlos
 y restarle 1 al exponente, si el signo de la función func_signo es negativo, multiplica el coeficiente por -1.
Si el exponente, el coeficiente o ambos son igual a 1, no los muestra.
 """

def respuesta_deriv(e,lista_signo):

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

def juego_deriv():
	
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

print("Temas:\n\n1. Derivación\n2. Integración\n\nEscoge el tema que te gustaría aprender (Escribe 1 o 2):\n")

key = getkey()

while key != "1" and key != "2":
    tema = print("Escribe 1 o 2:\n")
    key = getkey()

if key == "1":

	print("DERIVACIÓN")

	print("\nDeseas practicar este tema?\n\nS = Sí\n\nN = No\n")

	key = getkey()

	if key == "n" or key == "N":

		print("¡No hay problema!")

	while key == "s" or key == "S":

		juego_deriv()

		print("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n")

		key = getkey()

		if key == "n" or key == "N":

			print("¿Estás segur@?\n\nS = Sí\n\nN = No\n")

			key = getkey()

			if key == "s" or key == "S":

				key = "n" 
        
    #Cuando el usuario decide dejar de practicar este tipo de derivadas, se prosigue a las trigonométricas que están en otro archivo.

	print("¡De acuerdo!\n--------------------------------\n\nA continuación aprenderás a derivar funciones trigonométricas")

	exec(open("./trigo.py").read())

elif key == "2":

	print("INTEGRACIÓN\n\nEn proceso...")
