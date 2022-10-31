
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class EmpleadoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    cargo = StringField('Cargo')
    salario = StringField('Salario',validators=[DataRequired()])
    enviar = SubmitField('Enviar')

class ComidaForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    precio = StringField('Precio',validators=[DataRequired()])
    enviar = SubmitField('Enviar') 

class RestauranteForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    direccion = StringField('Direccion')
    capacidad = StringField('Capacidad',validators=[DataRequired()])
    gerente = StringField('Gerente',validators=[DataRequired()])
    enviar = SubmitField('Enviar')
