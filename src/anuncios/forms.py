from flask_wtf import FlaskForm
from wtforms import (
    StringField, TextAreaField, SubmitField,
    IntegerField, BooleanField, SelectField
)
from wtforms.validators import DataRequired, Email, Length, NumberRange

from wtforms.fields import DateField, TimeField


class FormularioEvento(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired(), Length(max=128)])
    slug = StringField("Slug", validators=[Length(max=128)])
    descripcion = TextAreaField("Descripción", validators=[DataRequired()])
    fecha = DateField("Fecha", format="%Y-%m-%d", validators=[DataRequired()])
    hora = TimeField("Hora", format="%H:%M", validators=[DataRequired()])
    lugar = StringField("Ubicación", validators=[DataRequired(), Length(max=128)])
    categoria = SelectField("Categoría", choices=[], validators=[DataRequired()])
    cupo_maximo = IntegerField("Cupo máximo", validators=[DataRequired(), NumberRange(min=1, max=100000)])
    destacado = BooleanField("Destacado")
    enviar = SubmitField("Guardar evento")

    # Alias en inglés por si alguna plantilla vieja los usa
    title = titulo
    description = descripcion
    date = fecha
    time = hora
    location = lugar
    category = categoria
    max_attendees = cupo_maximo
    submit = enviar


class FormularioRegistro(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired(), Length(max=64)])
    correo = StringField("Correo", validators=[DataRequired(), Email(), Length(max=128)])
    enviar = SubmitField("Registrarme")
