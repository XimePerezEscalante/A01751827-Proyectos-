"""Primero se muestra una introducción a cálculo junto con los temas disponibles"""

print("Cálculo Diferencial e Integral: Juega y aprende \n\nIntroducción \n\nCálculo es \
la matemática del cambio, de rectas tangentes, pendientes, áreas, volúmenes, \
longitudes de arcos, centroides, curvaturas, etc.\nA continuación se presentan\
los temas que se abordarán en este libro:\n1. Límites\n2. Derivación\n3. Integración")

tema = int(input("Escoge el tema que te gustaría aprender (Escribe 1, 2 o 3):\n"))

"""Después de que el usuario escoge el tema se le mostrará la explicación y
después se le preguntará si desea practicar"""

if tema == 1:
    print("Límites\n\nLos límites se definen como...\n")
    practicar = input("Deseas practicar este tema?\n\nPresiona la tecla S para practicar o la tecla N si deseas seguir leyendo o pasar a otro tema:\n")
    
    if practicar == "S" or practicar == "s":
        respuesta = int(input("Cada ronda tendrá 5 preguntas y cada una valdrá 2 puntos. Este es un ejemplo, escribe 1 para seguir.\n"))
        
        if respuesta == 1:
            puntos = 2
            print("¡Correcto!   +2pts")
        else:
            print("¡Incorrecto!   +0pts")
            puntos = 0
            
        respuesta = int(input("Este es un ejemplo, escribe 1 para seguir.\n"))
        
        if respuesta == 1:
            puntos = puntos + 2
            print("¡Correcto!   +2pts")
        else:
            if puntos == 0:
                puntos = puntos + 0
                print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   +0pts")
            else:
                puntos = puntos - 1
                print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   -1pt")
            
        """Al final el usuario puede ver cuántos puntos tiene en total"""
        
        print("Puntos = ",puntos)   
    elif practicar == "N" or practicar == "n":
    
        print("¡De acuerdo! Toma el tiempo que necesites hasta que te sientas list@ para practicar.")
    
    

elif tema == 2:
    print("Derivación\n\nLa derivación se define como...\n")
    practicar = input("Deseas practicar este tema?\n\nPresiona la tecla S para practicar o la tecla N si deseas seguir leyendo o pasar a otro tema:\n")
    if practicar == "S" or practicar == "s":
        respuesta = int(input("Cada ronda tendrá 5 preguntas y cada una valdrá 2 puntos. Este es un ejemplo, escribe 1 para seguir.\n"))
        
        if respuesta == 1:
            puntos = 2
            print("¡Correcto!   +2pts")
        else:
            print("¡Incorrecto!   +0pts")
            puntos = 0
            
        respuesta = int(input("Este es un ejemplo, escribe 1 para seguir.\n"))
        
        if respuesta == 1:
            puntos = puntos + 2
            print("¡Correcto!   +2pts")
        else:
            if puntos == 0:
                puntos = puntos + 0
                print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   +0pts")
            else:
                puntos = puntos - 1
                print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   -1pt")
            
        """Al final el usuario puede ver cuántos puntos tiene en total"""
        
        print("Puntos = ",puntos)
    elif practicar == "N" or practicar == "n":
    
        print("¡De acuerdo! Toma el tiempo que necesites hasta que te sientas list@ para practicar.")
    
    
    
    
elif tema == 3:
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
                
            respuesta = int(input("Este es un ejemplo, escribe 1 para seguir.\n"))
            
            if respuesta == 1:
                puntos = puntos + 2
                print("¡Correcto!   +2pts")
            else:
                if puntos == 0:
                    puntos = puntos + 0
                    print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   +0pts")
                else:
                    puntos = puntos - 1
                    print("¡Incorrecto! A partir de la segunda pregunta, por cada respuesta incorrecta se le restará 1 punto al usuario sólo si tiene más de 0 puntos.   -1pt")
                
            """Al final el usuario puede ver cuántos puntos tiene en total"""
            
            print("Puntos = ",puntos)
            
    elif practicar == "N" or practicar == "n":
    
        print("¡De acuerdo! Toma el tiempo que necesites hasta que te sientas list@ para practicar.")



    
