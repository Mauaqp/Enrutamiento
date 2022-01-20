from flask import Flask, render_template

app = Flask(__name__)

#Variables 
mensaje = "¡Dojo!"

#Ruta index
@app.route( '/', methods=['GET'] )
def paginaInicial():
    return render_template("index.html")

#Ruta Dojo
@app.route( '/dojo', methods=['GET'])
def imprimeDatos(mensaje=mensaje):
    print("server.py funciona correctamente")
    return mensaje

#Rutas Say
@app.route( '/say/<string:nombre>', methods=['GET'])
def imprimeHola(nombre):
    print("server.py funciona correctamente")
    return "<h1> Hola " + nombre + "</h1>"


#Rutas Repiten
@app.route( '/repeat/<int:numero>/<string:palabra>', methods=['GET'])
def repite(numero, palabra):
    rep = int(numero)
    return (("<h2><br>" + palabra + "</br></h2>")* rep)
        
#Mensaje de error


#Condicion para app.run
if __name__ == "__main__":
    app.run(debug=True)