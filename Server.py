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
    #print str(request.form["fileJsonStr"])
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
        #print str(objFile["carpeta"])
        arbolB = listaUsuarios.obtenerArbolB(objFile["user"])
        carpeta = arbolB.retornarNodoArbolB(objFile["idCarpeta"], objFile["carpeta"])    
        arbolAVL = carpeta.arbolAVL
        respuesta = arbolAVL.agregarAVL1(NodoAVL(objFile["fileName"],objFile["fileBytes"]),arbolB.carpeta)
        arbolAVL.graficarArbolAVL(arbolB.carpeta)
    else :    
        arbolAVL = listaUsuarios.obtenerArbolAVL(objFile["user"])   
        respuesta = arbolAVL.agregarAVL1(NodoAVL(objFile["fileName"],objFile["fileBytes"]),usuario.raizRoot)
        arbolAVL.graficarArbolAVL(usuario.raizRoot)    
    
    return respuesta

@app.route('/recuperarArchivo', methods=['POST'])
def recuperarArchivo():
    arbolAVL = listaUsuarios.obtenerArbolAVL(request.form["user"])   #retorna arbolAvl del usuario 
    #busca el nodo que contiene el archivo y lo asigna a la variable byteFile
    arbolAVL.buscarArchivo(arbolAVL.raiz, request.form["nombreArchivo"]) # Raiz del arbol y nombre archivo
    archivo = arbolAVL.byteFile 
    print "BYTES---" + str(archivo.archivo)
    objFile = {"fileName" : archivo.nombre , "fileBytes": archivo.archivo} 
    jsonFile = json.dumps(objFile, default = jsonDefault )
    return jsonFile


@app.route('/insertarCarpeta',methods=['POST']) 
def insertarNodoB():
    objCarpeta = request.json
    usuario = listaUsuarios.obtenerUsuario(objCarpeta["user"])
    raizB = listaUsuarios.obtenerArbolB(objCarpeta["user"])
    #raizB = listaUsuarios.obtenerArbolB(request.form["user"])
    if(raizB == None):
        raizB = ArbolB()   
    usuario.raizRoot.arbolB = raizB
    raizB.crearNodoInsertar(objCarpeta["id"], objCarpeta["nombre"]) #id del nombre.. generar id en java con un .hashcode()
    raizB.dibujarArbol(usuario.nombre) 
    return "true"

@app.route('/obtenerRaices',methods=['POST']) 
def obtenerRaices():
    raizAVL = listaUsuarios.obtenerArbolAVL(request.data)
    raizB = listaUsuarios.obtenerArbolB(request.data)
    raices = {'raizAVL': raizAVL ,'raizB': raizB}
    jsonString = json.dumps(raices, default = jsonDefault )
    #print str(jsonString)
    return jsonString

@app.route('/recuperarCarpeta',methods=['POST']) 
def recuperarCarpeta():
    objCarpeta = request.json
    #print objCarpeta
    arbolB = listaUsuarios.obtenerArbolB(objCarpeta["user"])
    carpeta = arbolB.retornarNodoArbolB(objCarpeta["idCarpeta"], objCarpeta["nombre"])    
    #carpetasHijas = carpeta.raizB.inicio
    objCarpeta = {"nombreCarpeta" : carpeta.nombreCarpeta , "idCarpeta": carpeta.idNombre} 
    jsonString = json.dumps(objCarpeta, default = jsonDefault )
    return jsonString
###################################RESPUESTAS##########################

#################################################################################################
   
@app.route('/hola',methods=['POST'])
def he():
    return "hola Mundo"+ str(request.form["dato"])

if __name__ == "__main__":
    #app.run(debug=True, host='192.10.1.1')
    #app.run(debug=True, host='192.168.1.3')
    app.run(debug=True, host='127.0.0.1')