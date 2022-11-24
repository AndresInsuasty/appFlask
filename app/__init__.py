from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect

from .models.ModeloLibro import ModeloLibro

app = Flask(__name__)

csrf = CSRFProtect()
db = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    print(request.method)
    print(request.form['username'])
    print(request.form['password'])
    return render_template('/auth/login.html')
    """
    if request.method=='POST':
        if  request.form['usuario'] == 'admin1' and request.form['password'] == '123456':
        # print(request.form['usuario'])
        # print(request.form['password'])
            return redirect(url_for('index'))
        else:
            return render_template('/auth/login.html')
    else:
        return render_template('/auth/login.html')

def pagina_no_encontrada(e):
    return render_template('errores/404.html'), 404

@app.route('/libros')
def listar_libros():
    try:
        libros = ModeloLibro.listar_libros(db)
        data = {'libros': libros}
        return render_template('listado_libros.html', data=data)
    except Exception as e:
        raise Exception(e)


def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
