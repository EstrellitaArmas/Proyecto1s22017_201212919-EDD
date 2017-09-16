class NodoAVL(object):
    def __init__ (self, nombre=None, archivo=None, izquierda=None, derecha=None , padre = None):
        self.nombre = nombre
        self.archivo = archivo
        self.FE = 0
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre
        self.raiz = None
        self.encontro = None
                    

class ArbolAVL(object):
    def __init__ (self):
            self.raiz = None
            valor = ""                

    def agregarAVL1(self, nuevoNodo, usuario): #nodo avl y usuario de la circular       
            temp = self.retornarAVL(nuevoNodo, usuario) 
            if temp == None:
                h = Logical(False)
                usuario.raizAVL.raiz = self.agregarAVL(usuario.raizAVL.raiz, nuevoNodo, h)
                print("nodo agregado correctamente")
            else:
                print("ya existe")
        
    def agregarAVL(self, raiz, nuevoNodo, h):
        if raiz == None:
            raiz = nuevoNodo            
            h.setLogical(True)
        elif int(nuevoNodo.nombre) < int(raiz.nombre):
            nodoIz = self.agregarAVL(raiz.izquierda, nuevoNodo, h)
            raiz.izquierda = nodoIz
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    raiz.FE = 0
                    h.setLogical(False)
                elif op == 0:
                    raiz.FE = -1
                elif op == -1:
                    nodo1 = raiz.izquierda
                    if nodo1.FE == -1:
                        raiz = self.rotacionII(raiz, nodo1)
                    else:
                        raiz = self.rotacionID(raiz, nodo1)
                    h.setLogical(False)
        elif int(nuevoNodo.nombre) > int(raiz.nombre):
            nodoDr = self.agregarAVL(raiz.derecha, nuevoNodo, h)
            raiz.derecha = nodoDr
            if h.getLogical() == True:
                op = raiz.FE
                if op == 1:
                    nodo1 = raiz.derecha
                    if nodo1.FE == 1:
                        raiz = self.rotacionDD(raiz, nodo1)
                    else:
                        raiz = self.rotacionDI(raiz, nodo1)
                    h.setLogical(False)
                elif op == 0:
                            raiz.FE = 1
                elif op == -1:
                    raiz.FE = 0
                    h.setLogical(False)
        return raiz    
    
    def retornarAVL(self, nuevoNodo, nodoCircular): 
        nodoCircular.raizAVL.encontro = None
        self.buscarAVL(nodoCircular.raizAVL.raiz, nuevoNodo, nodoCircular)
        return nodoCircular.raizAVL.encontro
    
    def buscarAVL(self, raiz, nuevoNodo, nodoCircular):  # raiz, nodo avl y nodo Circular
        if raiz != None:
            if nuevoNodo.nombre == raiz.nombre:
                nodoCircular.raizAVL.encontro = raiz
                #self.encontro = raiz
            else:
                self.buscarAVL(raiz.izquierda, nuevoNodo, nodoCircular)
                self.buscarAVL(raiz.derecha, nuevoNodo, nodoCircular)                    
                    
       
    def rotacionID(self, nodo, nodo1):
        nodo2 = nodo1.derecha
        nodo1.derecha = nodo2.izquierda
        nodo2.izquierda = nodo1
        nodo.izquierda = nodo2.derecha
        nodo2.derecha = nodo
        #nodo = nodo2
        if nodo2.FE == 1:
            nodo1.FE = -1
        else:
            nodo1.FE = 0
        if nodo2.FE == -1:
            nodo.FE = 1
        else:
            nodo.FE = 0
        nodo2.FE = 0
        return nodo2
    
    def rotacionII(self, nodo, nodo1):
        nodo.izquierda = nodo1.derecha
        nodo1.derecha = nodo
        if nodo1.FE == -1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = -1
            nodo1.FE = 1
        return nodo1
    
    def rotacionDD(self, nodo, nodo1):
        nodo.derecha = nodo1.izquierda
        nodo1.izquierda = nodo
        if nodo1.FE == 1:
            nodo.FE = 0
            nodo1.FE = 0
        else:
            nodo.FE = 1
            nodo1.FE = -1
        return nodo1
    
    def rotacionDI(self, nodo, nodo1):
        nodo2 = nodo1.izquierda
        nodo1.izquierda = nodo2.derecha
        nodo2.derecha = nodo1
        nodo.derecha = nodo2.izquierda
        nodo2.izquierda = nodo
    
        if nodo2.FE == 1:
            nodo.FE = -1
        else:
            nodo.FE = 0
        if nodo2.FE == -1:
            nodo1.FE = 1
        else:
            nodo1.FE = 0
        nodo2.FE = 0
        return nodo2    
                    
    def graficarArbolAVL(self, nodoCircular):
        nodoAVLTemp = nodoCircular.raizAVL
        self.digraf = "digraph G{\n"
        archivo = open("arbol.txt", 'w')
        self.graficarPreOrden(nodoAVLTemp.raiz)
        self.digraf += "\n}"
        archivo.write(self.digraf)
        archivo.close()

    def graficarPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            self.digraf += "nodo_" + str(nuevoNodo.nombre) + ' [label="' +str(nuevoNodo.nombre) +str(nuevoNodo.archivo) + '"]\n'
            if nuevoNodo.izquierda != None:
                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.izquierda.nombre) + "\n"
                self.graficarPreOrden(nuevoNodo.izquierda)
            else:
                pass
            if nuevoNodo.derecha != None:
                self.digraf += "nodo_" + str(nuevoNodo.nombre) + " -> " "nodo_" + str(nuevoNodo.derecha.nombre) + "\n"
                self.graficarPreOrden(nuevoNodo.derecha)                   
            else:
                pass
        else:
            pass

class Logical():
    def __init__ (self, valor=None):
        self.valor = valor
        
    def setLogical(self, valor):
        self.valor = valor
        
    def getLogical(self):
        return self.valor
