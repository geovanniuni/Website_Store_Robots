import pymysql
from flask.helpers import url_for
from flask import Flask,render_template,request,redirect,flash
from datetime import datetime


connection=pymysql.connect(
            host="18.222.42.25", # si es remota coloca IP // 192.168.200.50
            user='grupo',
            password='mysql',
            db='robots',)

cursor=connection.cursor()

sql='SELECT * FROM Producto'
try:
    cursor.execute(sql)
    data=cursor.fetchall() # mas de uno
    print(data)
except Exception as e:
    raise

sql='SELECT * FROM cliente'
try:
    cursor.execute(sql)
    data=cursor.fetchall() # mas de uno
    print(data)
except Exception as e:
    raise

def obtener_productos():
    #alumnosx = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM Producto")
            productox = cursor.fetchall()
            return productox
        except Exception as e:
            raise
    #return alumnosx


def obtener_clientes():
    #alumnosx = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM cliente")
            clientex = cursor.fetchall()
            return clientex
        except Exception as e:
            raise
    #return alumnosx

def insertar_cliente(idcliente,nombre_completo, correo, contrasenia,direccion,telefono):
    with connection.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO cliente_(idcliente_,nombre_completo, correo, contrasena,direccion,telefono) VALUES (%s, %s, %s, %s, %s, %s)",(idcliente,nombre_completo, correo, contrasenia,direccion,telefono))
            connection.commit()
        except Exception as e:
            raise
    
print(obtener_productos())


app = Flask(__name__)


@app.route('/')
def index():
   #return "Hello World"
   return render_template("index.html")

@app.route("/tienda")
def formulario_agregar_producto():
    return render_template("tienda.html")

@app.route("/estadisticas")
def resumen_estadisticas():
    producto = obtener_productos()
    return render_template("estadisticas.html",producto=producto )

# @app.route("/mispedidos")
# def formulario_agregar_alumno():
#     return render_template("mispedidos.html")

@app.route("/registro")
def formulario_agregar_cliente():
    return render_template("registro.html")


# #@app.route("/")
# @app.route("/estadisticas")
# def alumnos():
#     alumno = obtener_alumnos()
#     #return render_template("alumnos.html")
#     return render_template("alumnos.html", alumno=alumno)


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    idcliente = request.form["idcliente"]
    nombre_completo = request.form["nombre_completo"]
    correo = request.form["correo"]
    contrasenia = request.form["contrasenia"]
    direccion = request.form["direccion"]
    telefono = request.form["telefono"]
    insertar_cliente(idcliente, nombre_completo, correo, contrasenia, direccion, telefono)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/registro")










if __name__=="__main__":
    app.run(host='0.0.0.0', port=8050, debug=True)
