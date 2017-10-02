from ArbolAVL import ArbolAVL 
from ArbolB import ArbolB 
from ArbolB import NodoB 

class NodoDoble(object):
    def __init__(self, nombre = None , password= None, prox = None , ant = None):
        self.nombre = nombre 
        self.password = password
        #self.raizAVL = ArbolAVL()
        self.raizRoot = NodoB()    
        self.prox = prox
        self.ant = ant
    def __str__(self):
        return str(self.password, self.nombre, self.raizRoot)

class ListaDobleEnlazada(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nodo = None):
        if self.primero == None :
            self.primero = nodo
            self.ultimo = nodo
        else :
            nodo.prox = self.primero
            self.primero.ant = nodo 
            self.primero = nodo

        self.primero.ant = self.ultimo
        self.ultimo.prox = self.primero
       
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print "usuarios :"+ str(aux.nombre)
            aux = aux.prox  
            if aux == self.primero:
                break
        print "fin de la lista"

    def obtenerUsuario(self, nombre= None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                print "usuario encontrado :"+ str(aux.nombre)    
                return aux            
            aux = aux.prox
            if  aux == self.primero:
                return "false"

    def validarUser(self, nombre= None, password = None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre and aux.password == password:
                print "usuario encontrado :"+ str(aux.nombre)    
                return "true"            
            aux = aux.prox
            if  aux == self.primero:
                return "false"

    def obtenerArbolAVL(self, nombre = None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                return aux.raizRoot.arbolAVL           
            aux = aux.prox  
            if  aux == self.primero:
                return "false"

    def obtenerArbolB(self, nombre = None):
        aux = self.primero
        while aux != None:
            if aux.nombre == nombre:
                return aux.raizRoot.arbolB   ## Verificar que retorne un arbol B       
            aux = aux.prox  
            if  aux == self.primero:
                return "false"
