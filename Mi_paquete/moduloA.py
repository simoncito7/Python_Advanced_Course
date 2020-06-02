# curso avanzado Python

# presentación e introducción

# #--------------------------------------------------------------
# funciones y métodos

# print('\n' *100)			# Imprime cien espacios

# cadena = "  Hola José  "		# definición de "cadena"
# cadena2 = cadena.replace('Hola', 'Hola, cómo estás querido ')		# permite reemplazar un elemento de una cadena por otro. En este caso, se hace el reemplazo "Hola"----->"Hola, cómo estás querido "

# # print(cadena2)				# imprime cadena2

# # print(cadena.find("z"))		# imprime ubicación del elemento dado entre comillas, si es que existe. Si no existe, devolverá "-1"



# otramas = cadena.strip()		# Elimina los espacios al principio y al final de la cadena

# print(cadena)					# Imprime cadena con espacios
# print(otramas)					# Imprime cadena sin espacios

# otramasl=cadena.lstrip()		# Elimina espacios a la izquierda
# otramasr=cadena.rstrip()		# Elimina espacios a la derecha
# print(otramasl)					
# print(otramasr)
# otramasUpp=cadena.upper()		# LLeva todo a mayúsculas
# otramasLow=cadena.lower()		# Lleva todo a minúsculas
# print(otramasUpp)					
# print(otramasLow)

# cadena3 = 'Hola ? Hola, cómo estás ? querido '
# otramas2 = cadena3.split("?")					# Permite separar los elementos del string, sustituyendo el signo "?" por comas.
# print(otramas2)

# --------------------------------------------------------------------
# ordenamiento


# lista = [9,8,6,2,7,9,0,4]

# print(sorted(lista))		# Imprime lista ordenada
# print(sorted(lista,reverse=True))		# Imprime lista ordenada de forma inversa

# lista.sort()				# Ordena lista original
# print(lista)				

# Lista2 = ['Za', 'Fg', 'Az', 'Ij']
# print(sorted(Lista2))				# Imprime lista2 ordenada alfabéticamente
# Lista2.sort()						# ordena alfabéticamente la lista original
# print(Lista2)

#------------------------------------------------
#Declaración y manejo de conjuntos en python

# conjunto = set('8923')				# Permite tomar datos y crear un conjunto. Separa los elementos con una coma
# conjunto2 = {'8','1','5'}			# se crea un set de forma "manual"

# print(conjunto)
# print(conjunto2)
# print(conjunto & conjunto2)				# Imprime los elementos de la intersección entre los conjuntos dados
# print(conjunto.intersection(conjunto2))		# Imprime los elementos de la intersección entre los conjuntos dados

#---------------------------------------------------------------------------------

# MÓDULOS EN PYTHON

#----------------------------------------------------------------------------------
# creación de módulo

# def metodo():							# método creado y guardado en "modulo.py"
# 	print("Estamos usando M1")

# def metodo():							# método creado y guardado en "moduloN.py"
# 	print("Estamos usando M1")

# import modulo 						# se importa "modulo"
# import moduloN						# se importa "moduloN"

# modulo.metodo()					# Llamada al método contenido en "modulo.py"
# moduloN.metodo()				# Llamada al método contenido en "moduloN.py"

# import modulo as A 						# se importa "modulo" utilizando alias A
# import moduloN as B					# se importa "moduloN" utilizando alias B

# A.metodo()
# B.metodo()

# -----------------------------------
#variable path de Python

# import sys			#This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

# print(sys.path)		# Imprime los "paths" o rutas con las que puede trabajar Python y que necesita para poder ejecutarse (por ejemplo, para acceder a librerías).

#------------------------------------------
# manejo de paquetes con python

def metodoX():
	print("Estamos en A")

