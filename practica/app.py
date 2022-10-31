from ensurepip import version
from urllib.robotparser import RequestRate
from flask import Flask, request,url_for,render_template,redirect,session
from database import db
from flask_migrate import Migrate
from models import Bebida,Comida,Empleado,Mesa,Restaurante
from forms import ComidaForm,EmpleadoForm,RestauranteForm
import logging
import jsonify
logging.basicConfig(filename='info.log',  level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
app = Flask(__name__)

#Configuracion de la BD 
USER_DB = 'postgres'
PASS_DB = 'admin'
URL_DB = 'localhost'
NAME_DB= 'examen3'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

#configurar migracion
migrate = Migrate()
migrate.init_app(app,db)

#Form
app.config["SECRET_KEY"]="secret key"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def inicio():
#    if 'username' in session:
#        return redirect(url_for('index'))
#    else:
#        return redirect(url_for('login'))
    return render_template('index.html')


#se recargaba infinitamente al logear 


#@app.route('/login.html',methods=['GET','POST'])
#def login():
#    if request.method == "POST":
#        usuario = request.form["username"]
#        session['username'] = usuario
#        return redirect(url_for('/index.html'))
#    return render_template('login.html')
#Restaurantes



@app.route('/restaurantes.html')
def restaurantes():
    restaurantes = Restaurante.query.all()
    app.logger.debug(f'cargando restaurantes') 
   
    return render_template('restaurantes.html',restaurantes=restaurantes)




@app.route('/agregarrestaurante', methods=['GET','POST'])
def agregarrestaurante():
    restaurente = Restaurante()
    restauranteForm = RestauranteForm(obj=restaurente)
    if request.method =="POST":
        if restauranteForm.validate_on_submit():
            restauranteForm.populate_obj(restaurente)
            #insert
            db.session.add(restaurente)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a agregarrestaurante.html mandando:') 
    app.logger.debug(restauranteForm)  
    return render_template('agregarrestaurante.html',forma = restauranteForm)

@app.route('/editarrestaurante/<int:id>',methods=['GET','POST'])
def editarrestaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    restauranteForm = RestauranteForm(obj=restaurante)
    if request.method =="POST":
        if restauranteForm.validate_on_submit():
            restauranteForm.populate_obj(restaurante)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editarrestaurante.html mandando:') 
    app.logger.debug(restauranteForm) 
    return  render_template('editarrestaurante.html',forma =restauranteForm)

@app.route('/eliminarrestaurante/<int:id>')
def eliminarrestaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    db.session.delete(restaurante)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar restaurante') 
    app.logger.debug(restaurante) 
    return redirect(url_for('inicio'))


### Empleados

@app.route('/empleados.html')
def empleados():
    empleados = Empleado.query.all()
    app.logger.debug(f'cargando empleados') 
    return render_template('empleados.html',empleados=empleados)




@app.route('/agregarempleado', methods=['GET','POST'])
def agregarempleado():
    empleado = Empleado()
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method =="POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            #insert
            db.session.add(empleado)
            db.session.commit()
            return  redirect(url_for('inicio'))
    return render_template('agregarempleado.html',forma = empleadoForm)



@app.route('/editarempleado/<int:id>',methods=['GET','POST'])
def editarempleado(id):
    empleado = Empleado.query.get_or_404(id)
    empleadoForm = EmpleadoForm(obj=empleado)
    if request.method =="POST":
        if empleadoForm.validate_on_submit():
            empleadoForm.populate_obj(empleado)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editarempleado.html mandando:') 
    app.logger.debug(empleadoForm) 
    return  render_template('editarempleado.html',forma =empleadoForm)

@app.route('/eliminarempleado/<int:id>')
def eliminarempleado(id):
    empleado = Empleado.query.get_or_404(id)
    db.session.delete(empleado)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar empleado') 
    app.logger.debug(empleado) 
    return redirect(url_for('inicio'))

### Comidas

@app.route('/comidas.html')
def comidas():
    comidas = Comida.query.all()
    app.logger.debug(f'cargando comidas') 
    return render_template('comidas.html',comidas=comidas)




@app.route('/agregarcomida', methods=['GET','POST'])
def agregarcomida():
    comida = Comida()
    comidaForm = ComidaForm(obj=comida)
    if request.method =="POST":
        if comidaForm.validate_on_submit():
            comidaForm.populate_obj(comida)
            #insert
            db.session.add(comida)
            db.session.commit()
            return  redirect(url_for('inicio'))
    return render_template('agregarcomida.html',forma = comidaForm)




@app.route('/editarcomida/<int:id>',methods=['GET','POST'])
def editarcomida(id):
    comida = Comida.query.get_or_404(id)
    comidaForm = ComidaForm(obj=comida)
    if request.method =="POST":
        if comidaForm.validate_on_submit():
            comidaForm.populate_obj(comida)
            db.session.commit()
            return  redirect(url_for('inicio'))
    app.logger.debug(f'procediendo a editarcomida.html mandando:') 
    app.logger.debug(comidaForm) 
    return  render_template('editarcomida.html',forma =comidaForm)

@app.route('/eliminarcomida/<int:id>')
def eliminarcomida(id):
    comida = Comida.query.get_or_404(id)
    db.session.delete(comida)
    db.session.commit()
    app.logger.debug(f'procediendo a eliminar comida') 
    app.logger.debug(comida) 
    return redirect(url_for('inicio'))


#recibir json

@app.route('/restaurante',methods=['POST'])
def insertarresturante():
    token = request.headers.get('token')
    app.logger.debug("Token" + " " + token)
    info = request.get_json()
    nombre = info ["nombre"]
    direccion = info ["direccion"]
    capacidad = info ["capacidad"]
    gerente = info ["gerente"]
    return f'restaurante  {nombre} {direccion} {capacidad}{gerente}'
#enviar json

@app.route('/restaurate/<int:id>')
def mostrarRestaurante(id):
    valores = {"nombre": "unnombre","direccion": "unadireccion","capacidad": "unacapacidad","gerente": "ungerente","id": id}
    return jsonify(valores)