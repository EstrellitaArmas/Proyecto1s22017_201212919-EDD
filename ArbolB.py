from ArbolAVL import ArbolAVL 

class NodoB(object):
	def __init__(self, idNombre=None, nombreCarpeta=None):
		self.idNombre = idNombre
		self.nombreCarpeta = nombreCarpeta
		self.raizAVL = ArbolAVL()
		self.raizB = None

class Pagina(object): 
	def __init__(self, ramas=[0,0,0,0,0], claves=[0,0,0,0], cuentas=0):		
		self.ramas = ramas
		self.claves = claves
		self.cuentas = cuentas

class ArbolB(object):
	def __init__(self):
		self.inicio = Pagina()
		#self.inicio2 = Pagina()
		self.inserta = NodoB()
		self.enlace = Pagina()
		self.pivote = False
		self.existe = False
		self.existe2 = False
		self.encontrado = None
		
	#Crea el Nodo del Arbol B
	def crearNodoInsertar(self, idNombre, nombreCarpeta):
		nodob = NodoB(idNombre, nombreCarpeta)
		self.InsertarArbolB(nodob, self.inicio)
		
	
	#Inserta el nodo al Arbol B La clave es el Nodo y la raiz la Pagina
	def InsertarArbolB(self, clave, raiz):
		self.agregar(clave, raiz)
		if(self.pivote == True):
			self.inicio = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
			self.inicio.cuentas = 1
			self.inicio.claves[0] = self.inserta
			self.inicio.ramas[0] = raiz
			self.inicio.ramas[1] = self.enlace
			
			
	#Agregar al Arbol, Balanceando el arbol por Id
	def agregar(self, clave, raiz):
		pos = 0              
		self.pivote = False; 
		
		vacioBol = self.vacio(raiz)
		
		if(vacioBol == True):
			self.pivote = True
			self.inserta = clave
			self.enlace = None
		else:
			pos = self.existeNodo(clave, raiz)
			
			if(self.existe == True):
				self.pivote = False
			else:
				self.agregar(clave, raiz.ramas[pos])
				
				if(self.pivote == True):
					
					if(raiz.cuentas < 4):
						self.pivote = False;
						self.insertarClave(self.inserta, raiz, pos)
					else:
						self.pivote = True
						self.dividirPagina(self.inserta, raiz, pos)
						print("Inserto")
			
			
	#Verificar si la raiz no Existe
	def vacio(self, raiz):
		if(raiz == None or raiz.cuentas == 0):
			return True
		else:
			return False
		
	
	#Insertar Claves en Pagina
	def insertarClave(self, clave, raiz, posicion):
		i = raiz.cuentas
		
		while i != posicion:
			raiz.claves[i] = raiz.claves[i - 1]
			raiz.ramas[i + 1] = raiz.ramas[i]
			i-=1
		
		raiz.claves[posicion] = clave
		raiz.ramas[posicion + 1] = self.enlace
		val = raiz.cuentas+1
		raiz.cuentas = val
		print("Inserto Valor")
		
		
	#Dividir Pagina
	def dividirPagina(self, clave, raiz, posicion):
		pos = 0
		Posmda = 0
		if(posicion <= 2):
			Posmda = 2
		else:
			Posmda = 3
		
		Mder = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
		pos = Posmda + 1
		
		while pos != 5:
			i = ((pos - Posmda) - 1)
			j = (pos - 1)
			Mder.claves[i] = raiz.claves[j]
			Mder.ramas[pos - Posmda] = raiz.ramas[pos]
			pos+=1
		
		Mder.cuentas = 4 - Posmda
		raiz.cuentas = Posmda
		
		if(posicion <= 2):
			self.insertarClave(clave, raiz, posicion)
		else:
			self.insertarClave(clave, Mder, (posicion - Posmda))
			
		self.inserta = raiz.claves[raiz.cuentas - 1]
		Mder.ramas[0] = raiz.ramas[raiz.cuentas]
		val = raiz.cuentas - 1
		raiz.cuentas = val
		self.enlace = Mder
		
	
	#Virificar si Existe el Nodo	
	def existeNodo(self, clave, raiz):
		valor =0
		if(clave.idNombre < raiz.claves[0].idNombre):
			self.existe2 = False
			valor = 0
		else:
			valor = raiz.cuentas
			while (clave.idNombre < raiz.claves[valor - 1].idNombre and valor > 1):
				valor-=1
			
			if (clave.idNombre < raiz.claves[valor - 1].idNombre):
				self.existe = True
			else:
				self.existe = False
			
			if (clave.idNombre == raiz.claves[valor - 1].idNombre):
				self.existe2 = True
			else:
				self.existe2 = False			
			
		
		return valor
	
	#Virificar si Existe el Nodo	
	def existeCarpeta(self, clave, raiz): #clave = nod0 , raiz
		valor =0
		if(clave.idNombre < raiz.claves[0].idNombre):
			self.existe2 = False
			valor = 0
		else:
			valor = raiz.cuentas
			while (clave.idNombre < raiz.claves[valor - 1].idNombre and valor > 1):
				valor-=1
			
			if (clave.idNombre < raiz.claves[valor - 1].idNombre):
				self.existe = True
				self.encontrado = clave
			else:
				self.existe = False
			
			if (clave.idNombre == raiz.claves[valor - 1].idNombre):
				self.existe2 = True
				self.encontrado = clave
			else:
				self.existe2 = False			
			
		
		return valor


	#Crear Archivo
	def dibujarArbol(self):
		archivo=open('arbolB.dot', 'w')
		archivo.write('digraph G{\n')
		archivo.write("node [shape = record];\n");
		archivo.write("rankdir = TD;\n");
		self.grabarArchivo(self.inicio , archivo)
		archivo.write('}')
		archivo.close()	
		
	#Escribir Contenido del Archivo
	def grabarArchivo(self, raiz, archivo):
		nodo = raiz				
		if(nodo == None):
			print("No hay nada que Graficar")
		else:
			if (nodo.cuentas != 0):
				archivo.writelines("activo_" + str(nodo.claves[0].nombreCarpeta) + " [label= \"")
				k=1
				while k <= nodo.cuentas:
					archivo.writelines("<r" + str(k - 1) + ">" + " | " + "<cl" + str(k) + ">" + "IdArbol: " + str(nodo.claves[k - 1].nombreCarpeta) + " &#92;" + " | ")
					k+=1
				
				
				archivo.writelines("<r" + str(k - 1) + "> \"];\n")
				i=0
				while i <= nodo.cuentas:
					if (nodo.ramas[i] != None):
						if (nodo.ramas[i].cuentas != 0):
							archivo.writelines("activo_" + str(nodo.claves[0].nombreCarpeta) + ":r" + str(i) + " -> activo_" + str(nodo.ramas[i].claves[0].nombreCarpeta) + ";\n")							
						
					i+=1
					
				j=0
				while j <= nodo.cuentas:
					self.grabarArchivo(nodo.ramas[j],archivo)
					j+=1

	
					
					
					
					
	