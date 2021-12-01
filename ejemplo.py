import pymysql
from flask.helpers import url_for
from flask import Flask,render_template,request,redirect,flash
from datetime import datetime


connection=pymysql.connect(
            host="127.0.0.1", # si es remota coloca IP // 192.168.200.50
            user='root',
            password='810.768.sql.L2',
            db='unifiee',)

cursor=connection.cursor()

sql='SELECT * FROM alumno'
try:
    cursor.execute(sql)
    data=cursor.fetchall() # mas de uno
    print(data)
except Exception as e:
    raise


#sql='INSERT INTO alumno(nombre,nota,edad) VALUES (%s,%s,%s)'
#try:
#    cursor.execute(sql,("pedro",14,18))
#    connection.commit() # para confirmar en nuestra tabla
#            # o sino no se vera en la tabla solo en la consola
#except Exception as e:
#    raise


def obtener_alumnos():
    #alumnosx = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM alumno")
            alumnosx = cursor.fetchall()
            return alumnosx
        except Exception as e:
            raise
    #return alumnosx

def insertar_alumno(nombre, nota, edad):
    with connection.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO alumno(nombre, nota, edad) VALUES (%s, %s, %s)",(nombre, nota, edad))
            connection.commit()
        except Exception as e:
            raise
    
print("Hello World")


app = Flask(__name__)


@app.route('/')
def index():
   #return "Hello World"
   return render_template('indice.html')

@app.route("/agregar_alumno")
def formulario_agregar_alumno():
    return render_template("agregar_alumno.html")

#@app.route("/")
@app.route("/alumnos")
def alumnos():
    alumno = obtener_alumnos()
    #return render_template("alumnos.html")
    return render_template("alumnos.html", alumno=alumno)


@app.route("/guardar_alumno", methods=["POST"])
def guardar_alumno():
    nombre = request.form["nombre"]
    nota = request.form["nota"]
    edad = request.form["edad"]
    insertar_alumno(nombre, nota, edad)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/alumnos")


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)