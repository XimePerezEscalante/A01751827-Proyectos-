"""
Proyecto python.
Cálculo diferencial, juega y aprende.
El programa muestra una pequeña introducción a cálculo diferencial, junto con 
ejemplos y explicaciones para derivar. Después el usuario decide si quiere
practicar mediante un juego que tiene 5 preguntas por ronda, en el que se le 
muestra una ecuación a derivar, el programa la resuelve, la compara con la 
respuesta del usuario. Si la tiene bien se le suman 2 puntos y si falla, se
muestra la respuesta correcta.
"""

#Bibliotecas
import random
from random import randint

def func_signo():

	#Devuelve el signo utilizando la biblioteca random, si la ecuación tiene más de un elemento.

	signo = ["+","-"]
	signo_random = random.choice(signo)
	return signo_random

def func_literal():

	#Devuelve la literal que se usará en cada pregunta utilizando la biblioteca random.

	lista_literales = ["a","b","c","d","f","g","h","j","k","m","n","p","q","r","s","t","u","v","w","x","z"]
	literal = random.choice(lista_literales)
	return literal

def reescribir(lista,literal):

	"""
	Recibe la lista con el coeficiente en la posión 0 y el exponente en la posición 1,
	junto con la literal de la ecuación.
	Devuelve la ecuación reescrita.
	"""

	if lista[0] == 1:
		if lista[1] == 1:
			return literal
		else:
			return literal + "^" + str(lista[1])

	elif lista[0] == -1:
		if lista[1] == 1:
			return "-" + literal
		else:
			return "-" + literal + "^" + str(lista[1])

	else:
		if lista[1] == 1:
			return str(lista[0]) + literal
		else:
			return str(lista[0]) + literal + "^" + str(lista[1])

def suma_coef(suma):

	"""
	Recibe los coeficientes de los exponentes que se repiten para
	sumarlos
	"""
	i = 0
	for coef in suma:
		i = i + coef
	return i

def simplificar(exp,coef,literal):

	"""
	Recibe la lista de exponentes, la de coeficientes y la literal
	Devuelve la ecuación simplificada si es que hay exponentes repetidos,
	y si no los hay devuelve None 
	"""

	j = 0
	k = 1
	suma = []
	res_simp = []
	ecuacion_simp = []
	cont = 0

	while j < len(exp) - 1:
		if len(suma) != len(exp):
			
			while k < len(exp):
				if exp[j] == exp[k]:
					
					if cont == 0:
						suma.append(coef[j])
						
					suma.append(coef[k])
					cont = cont + 1
					exponente = exp[k]
				k = k + 1
		j = j + 1
		k = k - 1
	cont = 0

	if len(suma) > 0:

		coeFinal = suma_coef(suma)
		ecuacion_simp.append((coeFinal,literal,exponente))

		while cont < len(coef):	
			if exp[cont] != exponente:
				ecuacion_simp.append((coef[cont],literal,exp[cont]))
			cont = cont + 1
			
		return ecuacion_simp
	else:
		return None

def preguntas_deriv():

	#Devuelve la ecuación a derivar, de la complejidad dependerá el número de elementos a derivar.

	complejidad = randint(1,3)
	aux = complejidad
	ecuacion = []
	lista_coef = []
	lista_exp = []
	literal = func_literal()

	while complejidad > 0:
		coeficiente = randint(-9,9)
		exponente = randint(-9,9)

		while coeficiente == 0:
			coeficiente = randint(-9,9)

		lista_coef.append(coeficiente)
		lista_exp.append(exponente)
		ecuacion.append((coeficiente,literal,exponente))
		complejidad = complejidad - 1

	if aux > 1:
		ec_simp = simplificar(lista_exp,lista_coef,literal)
		if ec_simp != None:
			ecuacion = ec_simp
	return ecuacion

def respuesta_deriv(lista_derivar,lista_signo,literal):

	"""
	Recibe el coeficiente, el exponente de cada elemento y la literal de la ecuación a derivar.
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

	while cont <= len(lista_derivar):

		for i in lista_derivar:
			cont = cont + 1

			while num < len(lista_derivar):
				exp = lista_derivar[num][1]
				coef = lista_derivar[num][0]
				if exp == 0:
					if cont3 == 0 and len(lista_derivar) == 1:
						res.append("0")

				elif exp == 1:
					if len(lista_derivar) > 1:
						if cont3 == 1:
							signo2 = lista_signo[0]
							if signo2 == "-":
								coef = coef * -1
							if coef > 0:
								res.append(("+",str(coef)))
							else:
								res.append(str(coef))
								
						elif cont3 == 2:
							signo2 = lista_signo[1]
							if signo2 == "-":
								coef = coef * -1
							if coef > 0:
								res.append(("+",str(coef)))
							else:
								res.append(str(coef))
						else:
							res.append(str(coef))
					else:
						res.append(str(coef))
				else:
					exp = lista_derivar[num][1] - 1
					coef = lista_derivar[num][0] * lista_derivar[num][1]
					if len(lista_derivar) > 1:
						if cont3 == 1:
							signo2 = lista_signo[0]
							if signo2 == "-":
								coef = coef * -1
								
						elif cont3 == 2:
							signo2 = lista_signo[1]
							if signo2 == "-":
								coef = coef * -1
					derivada = reescribir([coef,exp],literal)

					if cont2 > 0:
						if coef > 0:
							res.append(("+",derivada))
						else:
							res.append((derivada))
					else:
						res.append((derivada))

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

	#Regresa la ecuación trigonométrica a derivar.

	ecuacion = []
	derivadaTrig = trigonometricas()
	coeficiente = randint(-9,9)
	literal = func_literal()
	exponente = randint(-9,9)

	while coeficiente == 0 or coeficiente == 1:
		coeficiente = randint(-9,9)

	while exponente == 1:
		exponente = randint(-9,9)

	ecuacion.append((derivadaTrig,coeficiente,literal,exponente))
	return ecuacion

def respuesta_deriv_trig(lista,trig,literal):

	"""
	Recibe la lista con el coeficiente y el exponente, la identidad trigonométrica y la literal
	Devuelve el resultado completo de la derivada
	"""

	lista_signo = []
	res = []
	original = reescribir(lista,literal)
	deriv_trig = {"sen":"cos","cos":"sen","tan":"sec^2","cot":"csc^2"}
	resultado = ""

	if lista[1] == 0:
		resultado = "0"
		
	else:
		if trig == "cos" or trig == "cot":
			lista[0] = lista[0] * -1
			derivar = [(lista[0],lista[1])]
			dy_dx = respuesta_deriv(derivar,lista_signo,literal)
			res = [dy_dx,deriv_trig[trig],"(",original,")"]
		elif trig == "csc":
			lista[0] = lista[0] * -1
			derivar = [(lista[0],lista[1])]
			dy_dx = respuesta_deriv(derivar,lista_signo,literal)
			res = [dy_dx,"csc(",original,")cot(",original,")"]
		elif trig == "sec":
			derivar = [(lista[0],lista[1])]
			dy_dx = respuesta_deriv(derivar,lista_signo,literal)
			res = [dy_dx,"sec(",original,")tan(",original,")"]
		else:
			derivar = [(lista[0],lista[1])]
			dy_dx = respuesta_deriv(derivar,lista_signo,literal)
			res = [dy_dx,deriv_trig[trig],"(",original,")"]
		for i in res:
			resultado += i + "" 
	return resultado

def mensaje(puntos):

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

	print("""Escribe la respuesta sin espacios y en el orden en que aparezca en la función.
Ejemplo:

	F(x) = 9x^3 + 6x - (-6x^4)

	Escribe el resultado de la siguiente manera:

	27x^2+6+24x^3

""")

	while cont2 < 5:
		cont2 = cont2 + 1
		cont3 = 1
		lista_signo = []
		lista_derivar = []
		print("--------------------------------\nPregunta",cont2,":\n\nf(x) = ",end = "")

		for n in preguntas_deriv():
			literal = n[1]
			
			if cont3 == 1:

				print(reescribir([n[0],n[2]],n[1]),end = " ")
				lista_derivar.append([n[0],n[2]])
				cont3 = cont3 + 1
			else:

				signo_final = func_signo()
				print(signo_final,"(",reescribir([n[0],n[2]],n[1]),")",end = " ")
				lista_derivar.append([n[0],n[2]])
				
			lista_signo.append(signo_final) 

			if len(lista_signo) == len(lista_derivar):
				lista_signo.pop(0)			

		respuesta = input("\n\nf'(x) = ")

		if respuesta == respuesta_deriv(lista_derivar,lista_signo,literal):
			print("\n¡Correcto!     +2pts\n")
			puntos = puntos + 2
		else:
			print("\n¡Incorrecto!     +0pts\n")
			print("RESULTADO:",respuesta_deriv(lista_derivar,lista_signo,literal),"\n")
			
	print("--------------------------------\nPuntos:",puntos,"\n")
	mensaje(puntos)

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
		lista_derivar = []	

		for n in preguntas_deriv_trig():

			literal = n[2]
			print(n[0],"(",reescribir([n[1],n[3]],n[2]),")",end = " ")
			lista_derivar.append(n[1])
			lista_derivar.append(n[3])

		respuesta = input("\nf'(x) = ")
		respuesta_correcta = respuesta_deriv_trig(lista_derivar,n[0],literal)

		if respuesta == respuesta_correcta:
			print("\n¡Correcto!     +2pts")
			puntos = puntos + 2

		else:
			print("\n¡Incorrecto!     +0pts")
			puntos = puntos + 0
			print("RESULTADO:",respuesta_correcta)
	print("--------------------------------\nPuntos:",puntos,"\n")
	mensaje(puntos)

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

practicar = input("\nDeseas practicar este tema?\n\nS = Sí\n\nN = No\n\n")

if practicar == "n" or practicar == "N":

	print("""
¡No hay problema!
Aquí hay más ejemplos:

	F(x) = 10x^-2

	f’(x) = -20x^-3
-------------------------------------------------------------------------------
	F(x) = 9x

	f'(x) = 9
-------------------------------------------------------------------------------

	F(x) = 8x^4 - 5x

	f'(x) = 32x^3 - 5
-------------------------------------------------------------------------------
""")

	practicar = input("""
Deseas practicar o pasar al siguiente tema?

S = Practicar

N = Siguiente tema

""")

while practicar == "S" or practicar == "s":
	juego_deriv()
	practicar = input("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n\n")
	if practicar == "n" or practicar == "N":
		practicar = input("\n¿Estás segur@?\n\nS = Sí\n\nN = No\n\n")
		if practicar == "s" or practicar == "S":
			practicar = "n"

print("""¡De acuerdo!
-------------------------------------------------------------------------------

A continuación aprenderás a derivar funciones trigonométricas:

		f’(sen u) = cos(u) * u'

		f’(cos u) = -sen(u) * u'

		f’(tan u) = sec^2(u) * u'

		f’(cot u) = -csc^2(u) * u'

		f’(sec u) = tan(u)sec(u) * u'

		f’(csc u) = -cot(u)csc(u) * u'

Ahora veamos ejemplos para cada función:


	Seno:

		F(x) = sen(4x^-8)

		f’(x) = -32x^-9cos(4x^-8)

	Coseno:

		F(x) = cos(-8x^-8)

		f’(x) = -64x^-9sen(-8x^-8)

	Tangente:

		F(x) = tan(-8x^9)

		f’(x) = -72x^8sec^2(-8x^9)

	Cotangente:

		F(x) = cot(9x^-3)

		f’(x) = 27x^-4csc^2(9x^-3)

	Secante:

		F(x) = sec(-9x^3)

		f’(x) = -27x^2sec(-9x^3)tan(-9x^3)

	Cosecante:

		F(x) = csc(-5x^7)

		f’(x) = 35x^6csc(-5x^7)cot(-5x^7)
""")

practicar = input("¿Deseas practicar este tema?\n\nS = Sí\n\nN = No\n\n")

while practicar == "S" or practicar == "s":
	juego_trig()
	practicar = input("\n¿Nuevo juego?\n\nS = Sí\n\nN = No\n")
	if practicar == "n" or practicar == "N":
		practicar = input("¿Estás segur@?\n\nS = Sí\n\nN = No\n")
		if practicar == "s" or practicar == "S":
			practicar = "n"
print("""¡De acuerdo!
-------------------------------------------------------------------------------""")
