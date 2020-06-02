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

# A.metodo()						# Llama al método que contiene utilizando el alias
# B.metodo()						# Llama al método que contiene utilizando el alias

# -----------------------------------
#variable path de Python

# import sys						# This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

# print(sys.path)					# Imprime los "paths" o rutas con las que puede trabajar Python y que necesita para poder ejecutarse (por ejemplo, para acceder a librerías).


#------------------------------------------
# manejo de paquetes con python

# from Mi_paquete import moduloA as A  # importa desde el paquete "Mi_paquete" el módulo "moduloA" y utilizo el alias "A"
# from Mi_paquete import moduloB as B  # importa desde el paquete "Mi_paquete" el módulo "moduloB" y utilizo el alias "B"

# A.metodoX()					# Llamo a método contenido en moduloA
# B.metodoY()					# Llamo a método contenido en moduloB

# ---------------------------------------------
# ARCHIVOS CSV EN PYTHON

# import csv

# doc=open("archivoW.csv","w")	# se define la variable doc mediante open(), donde se creará el archivoW.csv (si es que no existe). La "w" (write) indica que el archivo se podrá escribir
# doc_csv_w=csv.writer(doc)		# returns a writer object which writes data into CSV file

# lista=['pedro',99836]			# se define lista

# doc_csv_w.writerow(lista)		# escribe por fila la lista en doc
# doc.close()						# se cierra el archivo con el que se está trabajando
#------------------------------------------------------------------------
# en la siguiente forma se inserta cada elemento de lista2 en cada fila
# doc=open("archivoW.csv","w")	# se define la variable doc mediante open(), donde se creará el archivoW.csv (si es que no existe). La "w" (write) indica que el archivo se podrá escribir
# doc_csv_w=csv.writer(doc)		# returns a writer object which writes data into CSV file
# lista2=[["pedro",99836],["UNO",1000],["DOS",200000],["TRES",4000],["CUATRO",4000]]		# se define lista2
# doc_csv_w.writerows(lista2)		# escribe cada elemento de lista2 en una fila de doc (archivoW.csv)
# doc.close()				# cierra archivo que se está ejecutando
#-----------------------------------------------------------------------
# doc=open("archivoW.csv","w")	# se define la variable doc mediante open(), donde se creará el archivoW.csv (si es que no existe). La "w" (write) indica que el archivo se podrá escribir
# doc_csv_w=csv.writer(doc)		# returns a writer object which writes data into CSV file
# lista2=[['pedro',99836],["UNO",1000],["DOS",200000],["TRES",4000],["CUATRO",4000]]		# se define lista2

# for x in lista2:				# el bucle for recorrerá lista2 e irá escribiendo cada uno de los elementos de dicho arreglo en una fila del archivo .csv
# 	doc_csv_w.writerow(x)
# # la ventaja de usar el bucle es que podemos manipular o evaluar los datos antes de escribirlos en los archivos .csv

# doc.close()						# cierra archivo que se está ejecutando

#-----------------------------------------------------------------------
# doc=open("archivoW.csv","r")	# se define la variable doc mediante open(), donde se creará el archivoW.csv (si es que no existe). La "r" (read) indica que el archivo se podrá leer unicamente

# doc_csv=csv.reader(doc)

# for x in doc_csv:
# 	print(x)

# doc.close()



#-------------------------------------------------------------------------
# BASES DE DATOS EN PYTHON
# * primero se descargó XAMPWEB para tener MySQL
# * luego se baja un conector para Python y la base de datos

# creación de BBDD desde Python

# import mysql.connector		# se importa paquete "connector" 

# con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")		# Instrucción que permite lograr la conexión con la BBDD

# cursor=con.cursor() 	# esta instrucción nos permite interactuar con el servidor mysql usando el objeto MySQLConnection

# # cursor.execute("CREATE TABLE example(id INT, data VARCHAR(100));")		# Ejecuta las instrucciones de crear los campos id(INT) y DATA(CHAR)


# # con.close()		# Cierra la conexión con la BBDD

# #------------------------------------------------------------
# # ingresamos datos dentro de la BBDD creada

# cursor.execute("INSERT INTO example (id,data) VALUES ('34976238','Simon'), ('16079535','Susana'), ('7825080','Alfonzo');")		# se ejecuta la instrucción SQL que permitirá insertar el id "9" y el dato: "dato"
# # en SQL el entero va entre comillas simples.

# con.commit()	# permite asegurar que el cambio insertado sea guardado de forma efectiva
# con.close()		# close the conexion

# --------------------------------------------------------------
# leer datos de una BBDD desde Python

# import mysql.connector		# se importa paquete "connector" 

# con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")		# Instrucción que permite lograr la conexión con la BBDD

# cursor=con.cursor() 	# esta instrucción nos permite interactuar con el servidor mysql usando el objeto MySQLConnection

# cursor.execute("SELECT * FROM `example` WHERE `id`=9")		# selecciona de la tabla "example" todos los "id"=9

# rows = cursor.fetchall()				# fetchall() indica que extraiga todos los resultados de la query

# for row in rows:
# 	print(row)

# cursor.close()
# con.close()

#--------------------------------------------------------------------
# borrar datos de una BBDD utilizando Python

# importación de paquete "connector"
# import mysql.connector 

# # conexión con la BBDD "bd_python" que está en el host local
# cnx = mysql.connector.connect(user="root", password="",host="127.0.0.1", database="bd_python")

# #creación del cursor. Se recuerda que este método permite ejecutar sentencias SQL sobre la BBDD con la que se está trabajando.
# cursor = cnx.cursor()

# # se ejecuta el borrado del dato correspondiente a id=9 mediante comandos SQL
# cursor.execute("DELETE FROM `example` WHERE `id`=9; ")

# # se guardan los cambios efectuados
# cnx.commit()

# # se cierra el cursor
# cursor.close()

# # se cierra la conexión
# cnx.close()

# ------------------------------------------------------------------------
# Excelente tutorial de SQLite con Python en la siguiente URL: https://likegeeks.com/es/tutorial-de-python-sqlite3/

# SQLiteStudio con Python

# Comando SQL utilizado en SQLite Studio para crear la tabla "usuario" con los campos que están dentro de los corchetes
# CREATE TABLE "usuarios"("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "nombre" TEXT, "tipo" TEXT, "edad" INTEGER);

# importación de librería sqlite3
# import sqlite3	

# # creación de conexión
# con = sqlite3.connect('pythondb.db')

# cursor = con.cursor()

# query = "INSERT INTO 'usuarios' ('nombre', 'tipo', 'edad') VALUES ('José', 'normal', 28)"		# consulta de inserción de datos

# cursor.execute(query)

# con.commit()

# con.close()

# ejemplo 1

# import sqlite3 					# importación de método sqlite3

# from sqlite3 import Error

# # método de conexión con la BBDD
# def sql_connection():
	
# 	try:
# 		con = sqlite3.connect('mydatabase.db')
# 		return con

# 	except Error:

# 		print(Error)


# def sql_table(con):

#     cursorObj = con.cursor()

#     cursorObj.execute("INSERT INTO employees VALUES(3, 'Mariel', 1700, 'AD', 'Administrator', '2012-01-04')")

#     cursorObj.execute("CREATE TABLE if not exists employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")

#     con.commit()

# con = sql_connection()

# sql_table(con)

# ----------------------------------------------------------------------------------------------------------------------
# creación de la tabla "usuarios" y agregado de registros a la misma

# importación de librería
# import sqlite3
# #importación de método Error
# from sqlite3 import Error

# # método para llevar a cabo la conexión con la BBDD
# def sql_connection():
# 	# intenta conexión con BBDD
# 	try:
# 		cnx = sqlite3.connect('pythondb.db')
# 		return cnx
# 	# ejecuta una excepción
# 	except:
# 		print(Error)

# # método para crear una tabla o modificar elementos de la misma, en caso de estar creada
# def sql_table(cnx):

# 	cursor = cnx.cursor()		# #creación del cursor. Se recuerda que este método permite ejecutar sentencias SQL sobre la BBDD con la que se está trabajando.

# 	cursor.execute("CREATE TABLE if not exists usuarios(id integer PRIMARY KEY AUTOINCREMENT, name text, type text, age integer)")	# Se crea una tabla llamada "usuarios" (en caso de no existir)

# 	cursor.execute("INSERT INTO usuarios VALUES('5','Santiago', 'Maquinista', '51')") 

# 	cnx.commit()		# guarda los cambios efectuados

# 	cursor.close()

# 	cnx.close()

# cnx = sql_connection() 		# llamado a función encargada de la conexión

# sql_table(cnx)



#------------------------------------------------------------------------------------------------------------
# Lectura de datos de la BBDD

# import sqlite3
# #importación de método Error
# from sqlite3 import Error

# def sql_connection():
# 	# intenta conexión con BBDD
# 	try:
# 		cnx = sqlite3.connect('pythondb.db')
# 		return cnx
# 	# ejecuta una excepción
# 	except:
# 		print(Error)

# def table_query(cnx):

# 	cursor = cnx.cursor()

# 	# trae todos los datos de la BBDD
# 	for row in cursor.execute("SELECT * FROM 'usuarios'"):
# 		print(row)

# 	# en e siguiente caso traerá el usuario cuyo id sea "3"
# 	for row in cursor.execute("SELECT * FROM 'usuarios' WHERE id = 3"):
# 		print(row)

# 	# en este caso también traerá los datos correspondiente a un id específico, pero esta vez pasado por parámetro
# 	numID='2'
# 	for row in cursor.execute("SELECT * FROM 'usuarios' WHERE id = ?",numID):
# 		print(row)



# 	cursor.close()
# 	cnx.close()

# # llamado a la función para conectarme con la BBDD
# cnx = sql_connection()

# # Llamado a la función que me permite efectuar la query
# table_query(cnx)

# --------------------------------------------------------------------------------
# borrar uno o varios elementos de una BBDD

# import sqlite3
# #importación de método Error
# from sqlite3 import Error

# def sql_connection():
# 	# intenta conexión con BBDD
# 	try:
# 		cnx = sqlite3.connect('pythondb.db')
# 		return cnx
# 	# ejecuta una excepción
# 	except:
# 		print(Error)

# def table_query(cnx):

# 	cursor = cnx.cursor()

# 	# elimina el dato de la tabla "usuarios" de la BBDD correspondiente a id=2
# 	cursor.execute("DELETE FROM usuarios WHERE id=3")

# 	# guarda el cambio efectuado en la BBDD
# 	cnx.commit()

# 	# cierra el cursor
# 	cursor.close()

# 	# cierra la conexión con la BBDD
# 	cnx.close()

# # llamado a la función para conectarme con la BBDD
# cnx = sql_connection()

# # Llamado a la función que me permite efectuar la query
# table_query(cnx)


# ----------------------------------------------------------------------------------------
# INTERFACES GRÁFICAS EN PYTHON UTILIZANDO WXPYTHON
# instalación mediante anaconda: conda install -c anaconda wxpython

# # importación de librería wxpython
# import wx 			

# # creación de un objeto App()
# app = wx.App()

# # creación del contenedor Padre. "None" indica que "frame" es el contenedor padre. El "-1" indica a python que él asigne el id a cada elemento. El tercer parámetro es un título
# frame = wx.Frame(None,-1,'Primer ventana')

# # indica que se muestre la ventana "frame"
# frame.Show()

# # Creación de un "círculo infinito"
# app.MainLoop()


#-----------------------------------------------------------------------------------------

# # importación de librería wxpython
# import wx 			

# # creación de un objeto App()
# app = wx.App()

# # creación del contenedor Padre. "None" indica que "frame" es el contenedor padre. El "-1" indica a python que él asigne el id a cada elemento. El tercer parámetro es un título
# frame = wx.Frame(None,-1,'Primer ventana', style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

# # wx.MINIMIZE_BOX 	-------->	permite minimizar una ventana
# # wx.MAXIMIZE_BOX 	-------->	permite maximizar una ventana
# # wx.RESIZE_BORDER  -------->	permite modificar el tamaño de la interfaz
# # wx.SYSTEM_MENU    -------->	Displays a system menu containing the list of various windows commands in the window title bar.
# # wx.CAPTION 		 -------->	Puts a caption on the frame. Notice that this flag is required by wx.MINIMIZE_BOX, wx.MAXIMIZE_BOX and wx.CLOSE_BOX on most systems as the corresponding buttons cannot be shown if the window has no title bar at all. I.e. if wx.CAPTION is not specified those styles would be simply ignored.
# # wx.CLOSE_BOX		--------->	Permite que la interfaz pueda cerrarse con la "X"

# #

# # indica que se muestre la ventana "frame"
# frame.Show()

# # Creación de un "círculo infinito"
# app.MainLoop()

#--------------------------------------------------------------------------------
#utilización de un constructor para creación de una ventana

# importación de librería wxpython
# import wx 			

# # creación de clase con constructor, al cual se le están pasando el "None" para indicar que es la ventana padre y el título "hola". size(x,y)
# class Ventana(wx.Frame):
# 	def __init__(self,parent,title):
# 		super(Ventana,self).__init__(parent,title="segunda ventana", size=(800,300))
# 		#self.Centre()		# coloca la interfaz en medio de la pantalla
# 		self.SetPosition((10,10)) 	# coloca a la interfaz en x=10,y=10
# 		self.Show(True)		# instrucción para que la interfaz se muestre


# if __name__=='__main__':


# 	# creación de un objeto App()
# 	app = wx.App()

# 	vent = Ventana(None,title='Nueva ventana')

# 	# Creación de un "círculo infinito"
# 	app.MainLoop()

# creación del contenedor Padre. "None" indica que "frame" es el contenedor padre. El "-1" indica a python que él asigne el id a cada elemento. El tercer parámetro es un título
# frame = wx.Frame(None,-1,'Primer ventana', size=(400,400))



# # indica que se muestre la ventana "frame"
# frame.Show()

# Creación de un "círculo infinito"
# app.MainLoop()

	
#-------------------------------------------------------------------------------------------
# Definición de un menú para una ventana en Python

# # importación de la biblioteca wxpython
# import wx 			

# # class definition to create a menu bar
# class EjemploMenu(wx.Frame):
# 	# definición de constructor que recibe 3 elementos: "self", "parent" y "title".
# 	def __init__(self,parent,title):
# 		super(EjemploMenu,self).__init__(parent,title=title)

# 		# calling method when we're giving form to the menu bar
# 		self.InitUI()
	
# 	# GUI method
# 	def InitUI(self):

# 		# we create a MenuBar object
# 		menubar = wx.MenuBar()

# 		# we create a Menu object. The menu object will allow us to append a menu items into the menu
# 		fileMenu = wx.Menu()

# 		# 
# 		fileItem = fileMenu.Append(wx.ID_EXIT,'Salir','Salir de la App')

# 		menubar.Append(fileMenu,'&Archivo')

# 		self.SetMenuBar(menubar)

# 		# permite hacer un "enlace" (bind=enlazar)
# 		self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

# 		# permite que se muestre la interfaz
# 		self.Show(True)

# 	def OnQuit(self,e):

# 		self.Close()

# # creación del frame (objeto App)
# frame = wx.App()

# # llamado a la clase
# EjemploMenu(None,'Word')

# # creación del bucle de ejecución
# frame.MainLoop()

#-------------------------------------------------------------------------------------
# mejoramiento del menu wx en python


# importación de la biblioteca wxpython
# import wx 			

# # class definition to create a menu bar
# class EjemploMenu(wx.Frame):
# 	# definición de constructor que recibe 3 elementos: "self", "parent" y "title".
# 	def __init__(self,parent,title):
# 		super(EjemploMenu,self).__init__(parent,title=title)

# 		# calling method when we're giving form to the menu bar
# 		self.InitUI()
	
# 	# GUI method
# 	def InitUI(self):

# 		# we create a MenuBar object
# 		menubar = wx.MenuBar()

# 		# we create a Menu object. The menu object will allow us to append a menu items into the menu
# 		archivo = wx.Menu()

# 		# add the plugins to the bar
# 		archivo.Append(wx.ID_FILE,'&Archivo')
		
# 		archivo.Append(wx.ID_EDIT,'&Editar')
		
# 		archivo.Append(wx.ID_SAVE,'&Guardar')
		
# 		archivo.Append(wx.ID_HELP,'&Ayuda')
# 		# add a separator
# 		archivo.AppendSeparator()

# 		# we create another Menu object
# 		edit = wx.Menu()
# 		# these options (Zitem, Xitem and Witem) will be into "Editar" option
# 		edit.Append(wx.ID_ANY,'&Zitem')
# 		edit.Append(wx.ID_ANY,'&Xitem')
# 		edit.Append(wx.ID_ANY,'&Witem')

# 		# 
# 		archivo.AppendMenu(wx.ID_ANY,'&Editar',edit)

# 		opcion = wx.MenuItem(archivo,wx.ID_ANY,'&Salir')
# 		archivo.AppendItem(opcion)

# 		self.Bind(wx.EVT_MENU,self.OnQuit,opcion)
# 		menubar.Append(archivo,'&Archivo')

# 		self.SetMenuBar(menubar)
# 		self.Show(True)		

		

# 	def OnQuit(self,e):

# 		self.Close()

# # creación del frame (objeto App)
# frame = wx.App()

# # llamado a la clase
# EjemploMenu(None,'Word')

# # creación del bucle de ejecución
# frame.MainLoop()


#---------------------------------------------------------------------------------------
# lectura de datos desde una interfaz gráfica

# import wx 			

# # class definition to create a menu bar
# class EjemploTexto(wx.Frame):
# 	# definición de constructor que recibe 3 elementos: "self", "parent" y "title".
# 	def __init__(self,parent,title):
# 		super(EjemploTexto,self).__init__(parent,title=title)

# 		# calling method when we're giving form to the menu bar
# 		self.InitUI()
# 		# The GUI will be in the center of the screen
# 		self.Centre()
	
# 	# GUI method
# 	def InitUI(self):

# 		# we create a MenuBar object
# 		menubar = wx.MenuBar()

# 		# we create a Menu object. The menu object will allow us to append a menu items into the menu
# 		archivo = wx.Menu()

# 		# add the plugins to the bar
# 		archivo.Append(wx.ID_FILE,'&Archivo')
# 		archivo.Append(wx.ID_EDIT,'&Editar')		
# 		archivo.Append(wx.ID_SAVE,'&Guardar')		
# 		archivo.Append(wx.ID_HELP,'&Ayuda')
# 		# add a separator
# 		archivo.AppendSeparator()

# 		# we create another Menu object
# 		edit = wx.Menu()
# 		# these options (Zitem, Xitem and Witem) will be into "Editar" option
# 		edit.Append(wx.ID_ANY,'&Zitem')
# 		edit.Append(wx.ID_ANY,'&Xitem')
# 		edit.Append(wx.ID_ANY,'&Witem')

# 		# 
# 		archivo.AppendMenu(wx.ID_ANY,'&Editar',edit)

# 		opcion = wx.MenuItem(archivo,wx.ID_ANY,'&Salir')
# 		archivo.AppendItem(opcion)

# 		self.Bind(wx.EVT_MENU,self.OnQuit,opcion)
# 		menubar.Append(archivo,'&Archivo')

# 		self.SetMenuBar(menubar)

# 		self.panel = wx.Panel(self)
# 		# creates a grid with three rows and two columns
# 		self.sizer = wx.GridBagSizer(3,2)

# 		self.texto = wx.StaticText(self.panel, label = "Nombre: ")
# 		self.sizer.Add(self.texto, pos = (0,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5)

# 		self.textonuevo = wx.StaticText(self.panel, label = "Me llamo: ")
# 		self.sizer.Add(self.textonuevo, pos = (1,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5)

# 		self.textoedit = wx.TextCtrl(self.panel)
# 		self.sizer.Add(self.textoedit, pos = (0,1), span = (1,3), flag = wx.EXPAND | wx.LEFT | wx.BOTTOM, border = 5)

# 		self.boton = wx.Button(self.panel, label = "Enviar", size = (80,40))
# 		self.sizer.Add(self.boton, pos = (3,3), flag = wx.RIGHT | wx.BOTTOM)

# 		# Binds the method "TomarTexto" with the botton "boton"
# 		self.panel.Bind(wx.EVT_BUTTON, self.TomarTexto, self.boton)

# 		self.panel.SetSizerAndFit(self.sizer)

# 	def TomarTexto(self, event):

# 		textotomado = "Hola komo ta"
# 		textotomado = self.textoedit.GetValue()
# 		self.textonuevo.SetLabel(textotomado)


# 	def OnQuit(self,e):

# 		self.Close()

# # creación del frame (objeto App)
# app = wx.App(False)

# # llamado a la clase
# frame = EjemploTexto(None,'Word')

# frame.Show()

# # creación del bucle de ejecución
# app.MainLoop()


#--------------------------------------------------------------------------------------------------------
# ventana de login en Python

# import wx

# class EjemploTexto(wx.Frame):

# 	def __init__(self, parent):
# 		wx.Frame.__init__(self,parent)

# 		self.Centre()
		
# 		# we create a Panel type object
# 		self.panel = wx.Panel(self)		
# 		self.sizer = wx.GridBagSizer(3,2)

# 		self.textoU = wx.StaticText(self.panel, label= "User:" )		
# 		self.sizer.Add(self.textoU, pos = (0,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5)

# 		self.textoP = wx.StaticText(self.panel, label= "Password:" )
# 		self.sizer.Add(self.textoP, pos = (1,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5)

# 		self.textoR = wx.StaticText(self.panel, label= "Answer:" )
# 		self.sizer.Add(self.textoR, pos = (2,0), flag = wx.TOP | wx.LEFT | wx.BOTTOM, border = 5)

		

# 		self.textoeditU = wx.TextCtrl(self.panel)
# 		self.sizer.Add(self.textoeditU, pos = (0,1), span = (1,3), flag = wx.EXPAND | wx.BOTTOM)

# 		self.textoeditP = wx.TextCtrl(self.panel)
# 		self.sizer.Add(self.textoeditP, pos = (1,1), span = (1,3), flag = wx.EXPAND | wx.BOTTOM)



# 		self.boton = wx.Button(self.panel, label = "log in", size=(50,25))
# 		self.sizer.Add(self.boton, pos = (3,3), flag = wx.RIGHT | wx.BOTTOM)

# 		self.panel.Bind(wx.EVT_BUTTON, self.Validar, self.boton)
# 		self.panel.SetSizerAndFit(self.sizer)


# 	def Validar(self, event):
# 		usuario = self.textoeditU.GetValue()
# 		password = self.textoeditP.GetValue()

# 		if (usuario == 'jose' and password == 'jose'):
# 			self.textoR.SetLabel('Correcto')
# 			nv = NuevaVentana(None)
# 			nv.Show()
# 		else:
# 			self.textoR.SetLabel('Incorrecto')

# class NuevaVentana(wx.Frame):
# 	def __init__(self,parent):
# 		wx.Frame.__init__(self,parent)
# 		panel = wx.Panel(self,-1)
# 		txt = wx.StaticText(panel,label = "Entramos")

# app = wx.App(False)
# frame = EjemploTexto(None)
# frame.Show()
# app.MainLoop()


#------------------------------------------------------------------------------------
# urllib2	en python

# import urllib.request
# import urllib

# f = urllib.request.urlopen('http://www.python.org/')

# print(f.read(100).decode('utf-8'))

# response = urllib.request.urlopen('http://www.google.com.ar/')

# for line in response:
# 	print(line.rstrip())


#---------------------------------------------------
# scraping utilizando BeautifulSoup

# importación de BS
# from bs4 import BeautifulSoup
# # importación de librería requests
# import requests

# # se guarda en "url" la dirección del sitio al cual se quiere realizar la extracción
# url = input("Escribe el sitio web: ")
# # hace la petición al sitio web ingresado
# r=requests.get("http://"+url)
# # el resultado se almacena en data
# data=r.text

# # data se analiza con la librería de BS
# soup=BeautifulSoup(data)

# # se recorre con un ciclo for buscando todas las 'a'. Luego inprime todos los que regresen con un "href"
# # se recorre buscando la etiqueta "img" y con el "class_" indicado
# for link in soup.find_all('img',class_="attachment-home-post wp-post-image"):
# 	print(link.get('width'))

# 	print(link.get('href'))


#-----------------------------------------------------------
# ZEN DE PYTHON





