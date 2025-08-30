from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SubmitField,
    IntegerField, BooleanField, SelectField, DateField, TimeField
)
from wtforms.validators import DataRequired, Email, Length, NumberRange

class FormularioEvento(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired(), Length(max=128)])
    slug = StringField("Slug", validators=[Length(max=128)])
    descripcion = TextAreaField("Descripción", validators=[DataRequired()])
    fecha = DateField("Fecha", format="%Y-%m-%d", validators=[DataRequired()])
    hora = TimeField("Hora", format="%H:%M", validators=[DataRequired()])
    lugar = StringField("Ubicación", validators=[DataRequired(), Length(max=128)])
    categoria = SelectField("Categoría", choices=[], validators=[DataRequired()])
    cupo_maximo = IntegerField("Cupo máximo", validators=[DataRequired(), NumberRange(min=1, max=10000)])
    destacado = BooleanField("Destacado")
    enviar = SubmitField("Guardar evento")

class FormularioRegistro(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    correo = StringField("Correo", validators=[DataRequired(), Email()])
    enviar = SubmitField("Registrarme")
