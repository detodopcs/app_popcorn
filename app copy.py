from flask import Flask, render_template
import psycopg2


def conectar():
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        print("Conexion exitosa")
        cursor=connection.cursor()
        cursor.execute('SELECT version()')
        row=cursor.fetchone()
        #print(row)
        cursor.execute('SELECT * FROM Peliculas')
        rows=cursor.fetchall()        
        for row in rows:
            #return rows
            print(row)
    except Exception as ex:
        print(ex)
    finally:
        connection.close()
        print("conexion finalizada")

    return rows

conectar()














app = Flask(__name__)

"""
Configuración de la URI de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:salmo150@localhost/app_movies'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    contrasena = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    url_perfil = db.Column(db.String(255), nullable=False)

class Peliculas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)    
    fecha = db.Column(db.Date,nullable=False)
    calificacion = db.Column(db.Integer)
    url_fondo = db.Column(db.String(255), nullable=False)
    url_portada = db.Column(db.String(255), nullable=False)
    url_video = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(1), nullable=False)  

"""




@app.route("/")
def home():
   return render_template('index.html')

@app.route('/peliculas')
def peliculas():
   return render_template('peliculas.html')

@app.route('/series')
def series():
   return render_template('series.html')


@app.route('/mufasa')
def mufasa():
   return render_template('mufasa.html')


@app.route('/registro')
def registro():
   return render_template('registro.html')

@app.route('/login')
def login():
   return render_template('login.html')

#PAGINAS PARA USUATIOS REGISTRADOS

@app.route('/header')
def header_admin():
   return render_template('/admin/header_admin.html')

@app.route('/index-admin')
def index_admin():
   return render_template('/admin/index_admin.html')

@app.route('/pelicula-admin')
def pelicula_admin():
   return render_template('/admin/pelicula_admin.html')

@app.route('/series-admin')
def series_admin():
   return render_template('/admin/series_admin.html')

@app.route('/peliculas-list-admin')
def peliculas_list_admin():
   return render_template('/admin/peliculas_list.html')

@app.route('/dashboard')
def dashboard_admin():
   return render_template('/admin/dashboard.html')


@app.route('/footer')
def footer_admin():
   return render_template('/admin/footer_admin.html')



if __name__ == '__main__':
    app.run(debug=True)



"""
# Ruta para ejecutar la consulta y mostrar los resultados
def mostrar_usuarios():
    # Ejecutar la consulta
    _usuarios = usuarios.query.all()

    # Pasar los productos a la plantilla
    return render_template('productos.html', _usuarios=_usuarios)

def mostrar_peliculas():
    # Ejecutar la consulta
    __peliculas = Peliculas.query.all()
   

    # Pasar las peliculas a la plantilla
    return render_template('peliculas.html', _peliculas=__peliculas)

mostrar_peliculas()
"""