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
    usuario = request.json
    #usuario = json.loads(usuario)
    parametro = listaUsuarios.validarUser(usuario["user"],usuario["pass"])
    if parametro =="true":
        return "false"
    else:
        listaUsuarios.insertar(NodoDoble(usuario["user"],usuario["pass"]))
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

@app.route('/insertarArchivoTEMP',methods=['POST']) 
def insertarNodoAVLTEMP():
    #fileJson = request.form["fileJsonStr"]
    objFile = request.json
    usuario = listaUsuarios.obtenerUsuario(objFile["user"])  
    if(objFile["carpeta"] != "-"):
        print str(objFile["carpeta"])
        arbolB = listaUsuarios.obtenerArbolB(objFile["user"])
        arbolB.existeCarpeta(NodoB(objFile["idCarpeta"], objFile["carpeta"]),arbolB.inicio)
        arbolAVL = arbolB.carpeta.raizAVL
        respuesta = arbolAVL.agregarAVL1(NodoAVL(objFile["fileName"],objFile["fileBytes"]),arbolB.carpeta,False)
        arbolAVL.graficarArbolAVL(arbolB.carpeta)
    else :    
        arbolAVL = listaUsuarios.obtenerArbolAVL(objFile["user"])   
        respuesta = arbolAVL.agregarAVL1(NodoAVL(objFile["fileName"],objFile["fileBytes"]),usuario.raizRoot,False)
        arbolAVL.graficarArbolAVL(usuario.raizRoot)    
    
    return respuesta

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

@app.route('/recuperarCarpeta',methods=['POST']) 
def recuperarCarpeta():
    objCarpeta = request.json
    arbolB = listaUsuarios.obtenerArbolB(objCarpeta["user"])
    arbolB.existeCarpeta(objCarpeta["idCarpeta"],arbolB.inicio)
    #arbolAVL = arbolB.carpeta.raizAVL
    jsonString = json.dumps(arbolB.carpeta, default = jsonDefault )
    return jsonString

@app.route('/modificarCarpeta',methods=['POST']) 
def modificarCarpeta():
    objCarpeta = request.json
    arbolB = listaUsuarios.obtenerArbolB(objCarpeta["user"])
    arbolB.existeCarpeta(objCarpeta["idCarpeta"],arbolB.inicio)
    arbolB.carpeta.nombreCarpeta = objCarpeta["nombreCarpeta"] 
    jsonString = json.dumps(arbolB.carpeta, default = jsonDefault)
    return jsonString    

@app.route('/insertarCarpeta',methods=['POST']) 
def insertarNodoB():
    usuario = listaUsuarios.obtenerUsuario(request.data)
    raizB = listaUsuarios.obtenerArbolB(request.data)
    if( raizB == None):
        raizB = ArbolB()
    #raizB = listaUsuarios.obtenerArbolB(request.form["user"])
    #raizB.crearNodoInsertar(request.form["id"], request.form["nombre"], "C1")
    raizB.crearNodoInsertar(10, request.data)
    raizB.crearNodoInsertar(20, "Documentos")
    raizB.crearNodoInsertar(30, "Videos")  
    raizB.crearNodoInsertar(40, "APK")  
    raizB.crearNodoInsertar(50, "Archivos") 
    raizB.dibujarArbol() 
    usuario.raizRoot.raizB = raizB    
    return "true"

@app.route('/obtenerRaices',methods=['POST']) 
def obtenerRaices():
    raizAVL = listaUsuarios.obtenerArbolAVL(request.data)
    raizB = listaUsuarios.obtenerArbolB(request.data)
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
    app.run(debug=True, host='192.168.0.24')
    #app.run(debug=True, host='192.168.1.3')
    #app.run(debug=True, host='127.0.0.1')