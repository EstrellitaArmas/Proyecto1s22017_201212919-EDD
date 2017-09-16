class Nodo(object):
    def __init__(self, accion = None , prox = None):
        self.accion = accion
        self.prox = prox
    def __str__(self):
        return str(self.ip, self.mascara)

class ListaEnlazada(object):
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, nodo = None):
        if self.primero == None :
            self.primero = nodo
            self.ultimo = nodo
        else :
            self.ultimo.prox = nodo
            self.ultimo = nodo
       
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print "Nodo insertado :"+ str(aux.accion)
            aux = aux.prox    
