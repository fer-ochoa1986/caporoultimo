from flask import Flask,render_template,request, redirect, send_from_directory

# Importamos el módulo que permite conectarnos a la BS
import os
from flaskext.mysql import MySQL
#--------------------------------------------------------------------
# Creamos la aplicación
app = Flask(__name__)
CARPETA= os.path.join('uploads')
app.config['CARPETA']=CARPETA
#--------------------------------------------------------------------
# Creamos la conexión con la base de datos:
mysql = MySQL()
# Creamos la referencia al host, para que se conecte a la base
# de datos MYSQL utilizamos el host localhost
app.config['MYSQL_DATABASE_HOST']='localhost'
# Indicamos el usuario, por defecto es user
app.config['MYSQL_DATABASE_USER']='dais2015'
# Sin contraseña, se puede omitir
app.config['MYSQL_DATABASE_PASSWORD']='India1998'
# Nombre de nuestra BD
app.config['MYSQL_DATABASE_BD']='sistema'
# Creamos la conexión con los datos
mysql.init_app(app) 

@app.route('/')
def index():
 #-------------------------------------------------------
 # Hacemos una modificación para mostrar datos de la tabla
 # Empleados en la terminal...
 #-------------------------------------------------------

 # Creamos una variable que va a contener la consulta sql:
 sql = "SELECT * FROM `sistema`.`turnos`;"

 # Nos conectamos a la base de datos
 conn = mysql.connect()

 # Sobre el cursor vamos a realizar las operaciones
 cursor = conn.cursor()

 # Ejecutamos la sentencia SQL sobre el cursor
 cursor.execute(sql)

 # Copiamos el contenido del cursor a una variable
 db_turnos = cursor.fetchall()

 # "Commiteamos" (Cerramos la conexión)
 conn.commit()

 # Devolvemos código HTML para ser renderizado
 return render_template('turnos/create.html',turnos = db_turnos)



@app.route('/create')
def create():
 return render_template('turnos/create.html')


@app.route('/store', methods=['POST'])
def storage():
 # Recibimos los valores del formulario y los pasamos a variables locales:
 _nombre = request.form['txtNombre']
 _apellido = request.form['txtapellido']
 _correo = request.form['txtNcorreo']
 _turnoelegido = request.files['txtturnoelegido']
 _numerotelefono = request.files['txtnumerotelefono']

 # Y armamos una tupla con esos valores:
 datos = (_nombre,_correo,_apellido,_turnoelegido,_numerotelefono.filename)

 # Armamos la sentencia SQL que va a almacenar estos datos en la DB:
 sql = "INSERT INTO `sistematurno`.`turnos` \
  (`id`, `nombre`, `Ncelular`, `apellido`,`turnoelegido`) \
 VALUES (NULL, %s, %s, %s,%s);"
 conn = mysql.connect() # Nos conectamos a la base de datos
 cursor = conn.cursor() # En cursor vamos a realizar las operaciones
 cursor.execute(sql, datos) # Ejecutamos la sentencia SQL en el cursor
 conn.commit() # Hacemos el commit
 return render_template('turnos/create.html') # Volvemos a index.html



@app.route('/destroy/<int:id>')
def destroy(id):
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("DELETE FROM `sistema`.`turnos` WHERE id=%s", (id))
 conn.commit()
 return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):
 
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute("SELECT * FROM `sistema`.`turnos` WHERE id=%s", (id))
 turnos=cursor.fetchall()
 conn.commit()
 return render_template('turnos/edit.html', turnos=turnos)


@app.route('/update', methods=['POST'])
def update():
 _nombre=request.form['txtNombre']
 _correo=request.form['txtNcorreo']
 _apellido=request.files['txtapellido']
 _turnoelegido = request['txtturnoelegido']
 _numerotelefono =request['txtnumerotelefono']
 id=request.form['txtID']
 sql = "UPDATE `sistematurno`.`turnos` SET `nombre`=%s, `Ncelular`=%s, `apellido`=%s, `turnoelegido`=%s, WHERE id=%s;"
 datos=(_nombre,_correo,id,_apellido,_turnoelegido,_numerotelefono)
 conn = mysql.connect()
 cursor = conn.cursor()
 cursor.execute(sql,datos)
 conn.commit()
 return redirect('/')

@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
 return send_from_directory(app.config['CARPETA'], nombreFoto)


if __name__=='__main__':
 app.run(debug=True)

