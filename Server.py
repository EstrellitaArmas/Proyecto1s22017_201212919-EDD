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

def jsonDefault(object):
    return object.__dict__

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
    print str(request.form["fileJsonStr"])
    fileJson = request.form["fileJsonStr"]
    objFile = json.loads(fileJson)
    usuario = listaUsuarios.obtenerUsuario(request.form["user"])
    raiz = listaUsuarios.obtenerArbolAVL(request.form["user"])    
    raiz.agregarAVL1(NodoAVL(objFile["fileName"],objFile["fileBytes"]),usuario)
    raiz.graficarArbolAVL(usuario)
    return "true"

@app.route('/recuperarArchivo', methods=['POST'])
def recuperarArchivo():
    arbolAVL = listaUsuarios.obtenerArbolAVL(request.form["user"])   #retorna arbolAvl del usuario 
    #busca el nodo que contiene el archivo y lo asigna a la variable byteFile
    arbolAVL.buscarArchivo(arbolAVL.raiz, request.form["nombreArchivo"]) # Raiz del arbol y nombre archivo
    archivo = arbolAVL.byteFile 
    #print "BYTES---" + str(archivo.archivo)
    objFile = {"fileName" : archivo.nombre , "fileBytes": archivo.archivo} 
    jsonFile = json.dumps(objFile, default = jsonDefault )
    return jsonFile


@app.route('/insertarCarpeta',methods=['POST']) 
def insertarNodoB():
    raizB = listaUsuarios.obtenerArbolB("estergema")
    #raizB = listaUsuarios.obtenerArbolB(request.form["user"])
    #raizB.crearNodoInsertar(request.form["id"], request.form["nombre"], "C1")
    raizB.crearNodoInsertar(10, "Carpetas", "C1")
    raizB.crearNodoInsertar(20, "Documentos", "C2")
    raizB.crearNodoInsertar(30, "Videos", "C3")  
    raizB.crearNodoInsertar(40, "APK", "C4")  
    raizB.crearNodoInsertar(50, "Archivos", "C5") 
    raizB.crearNodoInsertar(60, "Carpetas", "C6")
    raizB.crearNodoInsertar(70, "Documentos", "C7")
    raizB.crearNodoInsertar(80, "Videos", "C8")  
    raizB.crearNodoInsertar(90, "APK", "C9")  
    raizB.crearNodoInsertar(100, "Archivos", "C10") 
    raizB.dibujarArbol() 
    return "true"

@app.route('/obtenerRaices',methods=['POST']) 
def obtenerRaices():
    raizAVL = listaUsuarios.obtenerArbolAVL(request.form["user"])
    raizB = listaUsuarios.obtenerArbolB(request.form["user"])
    raices = {'raizAVL': raizAVL ,'raizB': raizB}
    jsonString = json.dumps(raices, default = jsonDefault )
    print str(jsonString)
    return jsonString
###################################RESPUESTAS##########################

#################################################################################################
   
@app.route('/hola')
def he():
    return "hola Mundo"

if __name__ == "__main__":
    #app.run(debug=True, host='192.10.1.1')
    app.run(debug=True, host='192.168.1.3')
    #app.run(debug=True, host='127.0.0.1')