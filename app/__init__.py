from flask import Flask, render_template, request
app = Flask(__name__)


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
        print(request.form['usuario'])
        print(request.form['password'])
        return 'ok'
    else:
        return render_template('/auth/login.html')

def pagina_no_encontrada(e):
    return render_template('errores/404.html'), 404


def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    return app
