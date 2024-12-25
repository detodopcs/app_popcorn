from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session
import datetime
import psycopg2



def Obtener_peliculas():
    rows_peliculas = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )
        
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM Peliculas WHERE tipo=\'p\'')
        rows_peliculas=cursor.fetchall()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return rows_peliculas

def Obtener_series():
    rows_series = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor=connection.cursor()
        cursor.execute('SELECT * FROM Peliculas WHERE tipo=\'s\'')
        rows_series=cursor.fetchall()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return rows_series

def Obtener_Peliculas_Series_Resientes():
    rows_recientes = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )
        
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM Peliculas ORDER BY fecha DESC LIMIT 8')
        rows_recientes=cursor.fetchall()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return rows_recientes

def Obtener_Peliculas_Series_Recomendadas():
    rows_recomendadas = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor=connection.cursor()
        cursor.execute('SELECT * FROM Peliculas ORDER BY calificacion DESC LIMIT 8')
        rows_recomendadas=cursor.fetchall()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return rows_recomendadas

def Obtener_Peliculas_Por_Id(id):
    row_pelicula = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor=connection.cursor()
        cursor.execute(f'SELECT * FROM Peliculas WHERE id={id}')
        row_pelicula=cursor.fetchone()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return row_pelicula




def Obtener_Id_Por_Usuario_Contrasena(email, contrasena):
    row_pelicula = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor=connection.cursor()
        query = f"SELECT id FROM usuarios WHERE correo = '{email}' AND contrasena = '{contrasena}'"        
        cursor.execute(query)
        row_pelicula=cursor.fetchone()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return row_pelicula

def Obtener_Comentarios_Por_Pelicula(id):
    rows_comentarios = None
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor=connection.cursor()
        cursor.execute(f'SELECT c.*, u.nombre, p.titulo FROM Comentarios c INNER JOIN usuarios u ON c.id_usuario = u.id INNER JOIN Peliculas p ON c.id_pelicula = p.id WHERE c.id_pelicula={id}')
        rows_comentarios=cursor.fetchall()        
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close() 
    return rows_comentarios


def Registrar_Usuarios(nombre, email, contrasena, tipo_usuario):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor = connection.cursor()       
        sql = f"INSERT INTO usuarios(nombre, correo, contrasena, tipo, url_perfil) VALUES('{nombre}', '{email}', '{contrasena}', '{tipo_usuario}', 'https://w7.pngwing.com/pngs/825/857/png-transparent-computer-icons-user-profile-user-silhouette-apple-icon-image-format-user-profile-thumbnail.png' )"
             
        cursor.execute(sql)
        connection.commit()

    except psycopg2.Error as error: 
        print(f"Error al insertar el registro: {error}")
        connection.rollback() 

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def Validar_Login(email, contrasena):
    cuantos = 0
    try:
        connection=psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )
        
        cursor=connection.cursor()
        cursor.execute(f"SELECT COUNT(*) AS total_usuarios FROM usuarios WHERE correo='{email}' AND contrasena='{contrasena}'")
        cuantos= int(cursor.fetchone()[0])               
        
    except Exception as ex:
        print(ex)
    finally:
        connection.close()         
    return cuantos > 0

def Agregar_pelicula(titulo, descripcion, fecha, calificacion, url_fondo, url_portada, url_video, tipo):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor = connection.cursor()       
        sql = f"INSERT INTO Peliculas(titulo,descripcion,fecha,calificacion,url_fondo,url_portada,url_video,tipo) VALUES('{titulo}','{descripcion}','{fecha}','{calificacion}','{url_fondo}','{url_portada}','{url_video}','{tipo}')"
             
        cursor.execute(sql)
        connection.commit()

    except psycopg2.Error as error: 
        print(f"Error al insertar la pelicula o serie: {error}")
        connection.rollback() 

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



def Registrar_Comentario(comentario, pelicula_id, usuario_id):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='salmo150',
            database='app_movies'
        )

        cursor = connection.cursor()  
        hoy = datetime.datetime.now().strftime("%d/%m/%Y")     
        sql = f"INSERT INTO Comentarios(id_usuario, id_pelicula, descripcion, fecha) VALUES({usuario_id}, {pelicula_id}, '{comentario}','{hoy}')"
             
        cursor.execute(sql)
        connection.commit()

    except psycopg2.Error as error: 
        print(f"Error al insertar el comentario: {error}")
        connection.rollback() 

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/")
def app_start():   
   return redirect(url_for('home'))

@app.route("/home")
def home():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    data = {
        'recientes':Obtener_Peliculas_Series_Resientes(),
        'recomendadas':Obtener_Peliculas_Series_Recomendadas(),
        'usuario_logueado':usuario_logueado       
        }
    return render_template('index.html',peliculas=data)

@app.route('/peliculas')
def peliculas():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    _data={
        'peliculas':Obtener_peliculas(),        
        'usuario_logueado':usuario_logueado       
    }
    return render_template('peliculas.html',data =_data)

@app.route('/series')
def series():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    _data={
        'series':Obtener_series(),        
        'usuario_logueado':usuario_logueado       
    }
    return render_template('series.html',data =_data)  

@app.route('/pelicula_detalle')
def pelicula_detalle(): 
   usuario_logueado = {"email":session['email'], "contrasena":session['contrasena'], "id":session['id']} if 'email' in session else None
   query_id = request.args.get('id')
   _pelicula = Obtener_Peliculas_Por_Id(query_id)   
   _comentarios = Obtener_Comentarios_Por_Pelicula(query_id)   

   _datos ={ 
       "pelicula": _pelicula,
       "comentarios": _comentarios,
       "usuario_logueado":usuario_logueado 
   }

   return render_template('pelicula_detalle.html', datos = _datos)


@app.route('/registrar_comentario', methods=['POST'])
def registrar_comentario_post():   
   comentario= request.form['comentario'] 
   pelicula_id= request.form['pelicula_id'] 
   usuario_id= request.form['usuario_id'] 
   Registrar_Comentario(comentario, pelicula_id, usuario_id)
   return redirect(url_for('pelicula_detalle', id= pelicula_id))


@app.route('/registro')
def registro():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    _data={
        'usuario_logueado':usuario_logueado       
    }
    return render_template('registro.html',data =_data)

@app.route('/registro', methods=['POST'])
def registro_post():
   nombre= request.form['nombre']
   email= request.form['email']
   contrasena= request.form['contrasena']
   tipo_usuario= request.form['tipo_usuario']
   Registrar_Usuarios(nombre, email, contrasena, tipo_usuario)   
   return login()



@app.route('/login')
def login():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    _data={
        'usuario_logueado':usuario_logueado       
    }
    return render_template('login.html',data =_data)   

@app.route('/login', methods=['POST'])
def login_post():   
   email= request.form['email']
   contrasena= request.form['contrasena']
   
   if Validar_Login(email, contrasena):        
        session['email'] = email
        session['contrasena'] = contrasena
        id = Obtener_Id_Por_Usuario_Contrasena(email, contrasena)        
        session['id'] = id[0]
        return redirect(url_for('home'))
   else:
       return denegado()
   
@app.route('/logout')
def logout():
   session.pop('email', None) 
   session.pop('contrasena', None)
   session.clear()    
   return redirect(url_for('home'))


@app.route('/denegado')
def denegado():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    
    _data={
        'usuario_logueado':usuario_logueado       
    }
    return render_template('denegado.html',data =_data)   

@app.route('/dashboard')
def dashboard_admin():
    usuario_logueado = {"email":session['email'], "contrasena":session['contrasena']} if 'email' in session else None          
    
    if "email" not in session:
        return redirect(url_for("denegado")) 
    
    _data={
        'usuario_logueado':usuario_logueado       
    }
    return render_template('dashboard.html',data =_data)   

@app.route('/dashboard', methods=['POST'])
def dashboard_post():
   titulo= request.form['titulo']
   descripcion= request.form['descripcion']
   fecha= request.form['fecha']
   calificacion= request.form['calificacion']
   url_fondo= request.form['url_fondo']
   url_portada= request.form['url_portada']
   url_video= request.form['url_video']
   tipo= request.form['tipo']
   Agregar_pelicula(titulo, descripcion, fecha, calificacion, url_fondo, url_portada, url_video, tipo)    
   return dashboard_admin()



if __name__ == '__main__':
    app.run(debug=True)



