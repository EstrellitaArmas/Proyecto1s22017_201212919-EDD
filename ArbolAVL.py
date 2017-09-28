class NodoAVL(object):
    def __init__ (self, nombre=None, archivo=None, izquierda=None, derecha=None , padre = None):
        self.nombre = nombre
        self.archivo = archivo
        self.FE = 0
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre
        self.raiz = None
        
                    

class ArbolAVL(object):
    def __init__ (self):
            self.raiz = None
            valor = "" 
            self.byteFile = None  
            self.encontro = None             

    def agregarAVL1(self, nuevoNodo, carpeta): #nodo avl y carpeta de la circular       
            temp = self.retornarAVL(nuevoNodo, carpeta) 
            if temp == None:
                h = Logical(False)
                carpeta.raizAVL.raiz = self.agregarAVL(carpeta.raizAVL.raiz, nuevoNodo, h)
                print("nodo agregado correctamente"+ str(nuevoNodo.nombre))
            else:
                print("ya existe")
        
    def agregarAVL(self, raiz, nuevoNodo, h):
        if raiz == None:
            raiz = nuevoNodo            
            h.setLogical(True)
        elif nuevoNodo.nombre < raiz.nombre:
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
        elif nuevoNodo.nombre > raiz.nombre:
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
    
    def retornarAVL(self, nuevoNodo, carpeta): 
        carpeta.raizAVL.encontro = None
        self.buscarAVL(carpeta.raizAVL.raiz, nuevoNodo, carpeta)
        return carpeta.raizAVL.encontro
    
    def buscarAVL(self, raiz, nombre, carpeta):  # raiz, nodo avl y nodo Circular
        if raiz != None:
            if nombre == raiz.nombre:
                carpeta.raizAVL.encontro = raiz
                #self.encontro = raiz
            else:
                self.buscarAVL(raiz.izquierda, nombre, carpeta)
                self.buscarAVL(raiz.derecha, nombre, carpeta) 

                    
       
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
                    
    def graficarArbolAVL(self, carpeta):
        nodoAVLTemp = carpeta.raizAVL
        self.digraf = "digraph G{\n"
        archivo = open("arbol.dot", 'w')
        self.graficarPreOrden(nodoAVLTemp.raiz)
        self.digraf += "\n}"
        archivo.write(self.digraf)
        archivo.close()

    def graficarPreOrden(self, nuevoNodo):
        if nuevoNodo != None:
            mensajeFin = nuevoNodo.nombre.replace(".", "")
            mensajeFin = mensajeFin.replace("-", "")
            mensajeFin = mensajeFin.replace("_", "")
            mensajeFin = mensajeFin.replace(" ", "")
            self.digraf += "nodo_" + str(mensajeFin) + ' [label="' +str(mensajeFin) +'"]\n'
            if nuevoNodo.izquierda != None:
                mensajeIzq = nuevoNodo.izquierda.nombre.replace(".", "")
                mensajeIzq = mensajeIzq.replace("-", "")
                mensajeIzq = mensajeIzq.replace("_", "")
                mensajeIzq = mensajeIzq.replace(" ", "")
                self.digraf += "nodo_" + str(mensajeFin) + " -> " "nodo_" + str(mensajeIzq) + "\n"
                self.graficarPreOrden(nuevoNodo.izquierda)
            else:
                pass
            if nuevoNodo.derecha != None:
                mensajeDer = nuevoNodo.derecha.nombre.replace(".", "")
                mensajeDer = mensajeDer.replace("-", "")
                mensajeDer = mensajeDer.replace("_", "")
                mensajeDer = mensajeDer.replace(" ", "")
                self.digraf += "nodo_" + str(mensajeFin) + " -> " "nodo_" + str(mensajeDer) + "\n"
                self.graficarPreOrden(nuevoNodo.derecha)                   
            else:
                pass
        else:
            pass

    def buscarArchivo(self, raiz, nombre):  # raiz nodo avl y nombre del archivo
        if raiz != None:
            if nombre == raiz.nombre:
                self.byteFile = raiz
            else:
                self.buscarArchivo(raiz.izquierda, nombre)
                self.buscarArchivo(raiz.derecha, nombre) 

class Logical():
    def __init__ (self, valor=None):
        self.valor = valor
        
    def setLogical(self, valor):
        self.valor = valor
        
    def getLogical(self):
        return self.valor
