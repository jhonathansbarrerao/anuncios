from flask import Flask, render_template, request, redirect, url_for, abort, flash
from datetime import datetime

try:
    from .forms import FormularioEvento, FormularioRegistro
except ImportError:
    from forms import FormularioEvento, FormularioRegistro

app = Flask(__name__)
app.config["SECRET_KEY"] = "unaclave"

categorias = ["Tecnología", "Académico", "Cultural", "Deportivo", "Social"]

eventos = [
    {
        "id": 1,
        "titulo": "Conferencia de IA",
        "slug": "conferencia-IA",
        "descripcion": "Charla introductoria sobre IA y Flask.",
        "fecha": "2025-09-15",
        "hora": "14:00",
        "lugar": "Auditorio Principal",
        "categoria": "Tecnología",
        "cupo_maximo": 3,
        "asistentes": [
            {"nombre": "Nicolás Galvez", "correo": "Nico123@gmail.com"}
        ],
        "destacado": True,
    }
]

def generar_slug(texto: str) -> str:
    return (
        texto.lower()
        .replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        .replace("ñ", "n").replace(" ", "-")
    )

def buscar_evento_por_slug(slug: str):
    return next((e for e in eventos if e["slug"] == slug), None)

def dt_evento(e) -> datetime:
    return datetime.strptime(f'{e["fecha"]} {e["hora"]}', "%Y-%m-%d %H:%M")

def es_proximo(e) -> bool:
    try:
        return dt_evento(e) >= datetime.now()
    except Exception:
        return True

def siguiente_id() -> int:
    return (max([e["id"] for e in eventos]) + 1) if eventos else 1

@app.route("/")
def inicio():
    proximos = [e for e in eventos if es_proximo(e)]
    proximos.sort(key=lambda e: (not e.get("destacado", False), e["fecha"], e["hora"]))
    return render_template("index.html", eventos=proximos, categorias=categorias)

@app.route("/event/<string:slug>/")
def detalle_evento(slug):
    evento = buscar_evento_por_slug(slug)
    if not evento:
        abort(404)
    restantes = max(evento["cupo_maximo"] - len(evento["asistentes"]), 0)
    return render_template("detalle.html", evento=evento, restantes=restantes, categorias=categorias)

@app.route("/admin/event/", methods=["GET", "POST"])
def crear_evento():
    form = FormularioEvento()
    form.categoria.choices = [(c, c) for c in categorias]

    if form.validate_on_submit():
        titulo = form.titulo.data.strip()
        slug = (form.slug.data or "").strip() or generar_slug(titulo)

        if buscar_evento_por_slug(slug):
            flash("Ya existe un evento con ese slug. Cambia el título o el slug.", "error")
            return render_template("form_evento.html", form=form, categorias=categorias)

        evento = {
            "id": siguiente_id(),
            "titulo": titulo,
            "slug": slug,
            "descripcion": form.descripcion.data.strip(),
            "fecha": form.fecha.data.strftime("%Y-%m-%d"),
            "hora": form.hora.data.strftime("%H:%M"),
            "lugar": form.lugar.data.strip(),
            "categoria": form.categoria.data,
            "cupo_maximo": form.cupo_maximo.data,
            "asistentes": [],
            "destacado": bool(form.destacado.data),
        }
        eventos.append(evento)
        flash("Evento creado correctamente.", "success")
        return redirect(url_for("detalle_evento", slug=slug))

    return render_template("form_evento.html", form=form, categorias=categorias)

@app.route("/admin/events/")
def alias_admin_events():
    return redirect(url_for("crear_evento"))

@app.route("/event/<string:slug>/register/", methods=["GET", "POST"])
def registrar_evento(slug):
    evento = buscar_evento_por_slug(slug)
    if not evento:
        abort(404)

    restantes = evento["cupo_maximo"] - len(evento["asistentes"])
    if restantes <= 0:
        flash("Este evento ya alcanzó el cupo máximo.", "error")
        return redirect(url_for("detalle_evento", slug=slug))

    form = FormularioRegistro()
    if form.validate_on_submit():
        nuevo = {
            "nombre": form.nombre.data.strip(),
            "correo": form.correo.data.strip().lower(),
        }

        if any(a["correo"] == nuevo["correo"] for a in evento["asistentes"]):
            flash("Ese correo ya está registrado en este evento.", "error")
            return redirect(url_for("detalle_evento", slug=slug))

        if len(evento["asistentes"]) >= evento["cupo_maximo"]:
            flash("Cupo alcanzado justo ahora. Intenta con otro evento.", "error")
            return redirect(url_for("detalle_evento", slug=slug))

        evento["asistentes"].append(nuevo)
        flash("¡Registro exitoso!", "success")
        return redirect(url_for("detalle_evento", slug=slug))

    return render_template("form_registro.html", evento=evento, form=form, categorias=categorias)

@app.route("/events/category/<string:categoria>/")
def eventos_por_categoria(categoria):
    if categoria not in categorias:
        abort(404)
    filtrados = [e for e in eventos if e["categoria"] == categoria and es_proximo(e)]
    filtrados.sort(key=lambda e: (not e.get("destacado", False), e["fecha"], e["hora"]))
    return render_template(
        "por_categoria.html",
        categoria=categoria,
        eventos=filtrados,
        categorias=categorias
    )

if __name__ == "__main__":
    app.run(debug=True, port=5000)
