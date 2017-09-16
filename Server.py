import json , requests
from flask import Flask, request
from ListaDobleEnlazada import ListaDobleEnlazada 
from ListaDobleEnlazada import NodoDoble 
from ArbolAVL import ArbolAVL 
from ArbolAVL import NodoAVL 
from ListaEnlazada import ListaEnlazada 
from ListaEnlazada import Nodo
from ArbolB import NodoB
from ArbolB import ArbolB
from ArbolB import Pagina

app = Flask("server")

##########################################DASHBOARD###################

listaUsuarios = ListaDobleEnlazada()
bitacora = ListaEnlazada()
claseArbol = ArbolB()

@app.route('/insertarUsuario',methods=['POST']) 
def insertarUsuario():
    parametro = listaUsuarios.validarUser(request.form["user"],request.form["pass"])
    if parametro =="true":
        return "false"
    else:
        listaUsuarios.insertar(NodoDoble(request.form["user"],request.form["pass"]))
        listaUsuarios.imprimir()
        return "true"
    
    
@app.route('/validarUsuario',methods=['POST']) 
def validarUsuario():
    parametro = listaUsuarios.validarUser(request.form["user"],request.form["pass"])
    if parametro =="true":
        return "true"
    else:
        return "false"

@app.route('/insertarArchivo',methods=['POST']) 
def insertarNodoAVL():
    raiz = listaUsuarios.obtenerRaiz("estergema")
    usuario = listaUsuarios.obtenerUsuario("estergema")
    raiz.agregarAVL1(NodoAVL(request.data,"archivo.jpg"),usuario)
    raiz.graficarArbolAVL(usuario)
    #raiz.pruebaMostrarAVL()
    return "true"
    

@app.route('/insertarCarpeta',methods=['POST']) 
def insertarNodoB():
    claseArbol.crearNodoInsertar(10, "Carpetas", "C1")
    claseArbol.crearNodoInsertar(20, "Documentos", "C2")
    claseArbol.crearNodoInsertar(30, "Videos", "C3")  
    claseArbol.crearNodoInsertar(40, "APK", "C4")  
    claseArbol.crearNodoInsertar(50, "Archivos", "C5") 
    claseArbol.dibujarArbol() 
    return "true"

###################################RESPUESTAS##########################

#################################################################################################
   
@app.route('/hola')
def he():
    return "hola Mundo"

if __name__ == "__main__":
    #app.run(debug=True, host='192.10.1.1')
    app.run(debug=True, host='192.168.1.3')
    ##app.run(debug=True, host='127.0.0.1')