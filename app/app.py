# Import package
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

# Inicializamos una aplicación
app = Flask(__name__)

# CONFIG MYSQL → CONNECTION DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask-01'

conn = MySQL(app)

# Realizar peticiones antes y después de una petición
@app.before_request
def bofore_request():
    print('Antes de la peticion')

@app.after_request
def after_request(response):
    print('Despues de la Petición')
    return response

# Url Home → Index
@app.route('/')
def index():
    cursos = ['Python', 'JavaScript', 'TypeScript', 'Angular', 'Ionic', 'Java']
    geo = {
        'title': 'Index',
        'welcome': 'Lista de cursos',
        'cursos': cursos,
        'num_cursos': len(cursos)
    }
    # return '<h1>Run server...</h1>'
    return render_template('index.html', data=geo)

#Construcción de Url dinámicas con parámetros 
# http://localhost:5001/contact/Geo

@app.route('/contact/<name>/<int:edad>')
def get_contact(name, edad):
    data = {
        'title': 'Contacto',
        'name': name,
        'edad': edad
    }
    return render_template('contact.html', data=data)

# Se puede pasar varios parametros
# http://localhost:5001/query_string?param1=geo
# http://localhost:5001/query_string?param1=geo&param2=23

def query_string():
    print(request) # Obj request → Peticion
    print(request.args) # Argumentos
    print(request.args.get('param1')) # Nombre del Parametro enviado por URL
    print(request.args.get('param2')) # Nombre del Parametro enviado por URL
    return 'OK'

@app.route("/courses")
def courses_list():
    data = {}
    try:
        cursor = conn.connection.cursor()
        sql = 'SELECT * FROM cursos ORDER BY name ASC' # Buena práctica → Probar consulta en MySql
        cursor.execute(sql)
        cursos = cursor.fetchall()
        # print(cursos)
        data['cursos'] = cursos
        data['message']='OK'
    except Exception as ex:
        data['message']='ERROR'
    return jsonify(data)

# ERROR 404
def page_not_found(error):
    # return render_template('404.html'), 404 # Mostrar una plantilla
    return redirect(url_for('index')) # Redireccionar a otra url

# Comprobamos si estamos desde el archivo inicial (main)
# Ejecutamos la aplicación
if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug = True, port = 5001)







