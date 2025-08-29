# Aplicación Web de Anuncios

Una aplicación web simple para gestionar anuncios construida con Flask.

## Descripción General del Proyecto

Este proyecto es una aplicación web que permite a los usuarios crear y ver anuncios. Incluye funcionalidades de registro de usuarios y características de gestión de anuncios.

## Requisitos

- Python 3.12 o superior
- Gestor de paquetes Rye
- Git

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/jhonathansbarrerao/anuncios.git
cd anuncios
```

### 2. Instalar Dependencias con Rye

Este proyecto utiliza Rye para la gestión de dependencias. Si no tienes Rye instalado, puedes instalarlo siguiendo las instrucciones en la [documentación oficial de Rye](https://rye-up.com/guide/installation/).

```bash
# Sincronizar dependencias y crear entorno virtual
rye sync
```

## Ejecutar la Aplicación

### Configurar Variables de Entorno

#### Unix/Linux/macOS

```bash
export FLASK_APP=src/anuncios/run.py
export FLASK_ENV=development  # Usar 'production' para entorno de producción
```

#### Windows (Command Prompt)

```cmd
set FLASK_APP=src\anuncios\run.py
set FLASK_ENV=development
```

#### Windows (PowerShell)

```powershell
$env:FLASK_APP = "src\anuncios\run.py"
$env:FLASK_ENV = "development"
```

### Iniciar la Aplicación

```bash
# Activar el entorno virtual (si no se usa rye run)
. .venv/bin/activate  # En Unix/Linux/macOS
. .venv\Scripts\activate  # En Windows

# Ejecutar la aplicación
flask run

# Alternativamente, cuando no se usa entorno virtual
flask --app src/anuncios/run.py run
```

La aplicación estará disponible en http://127.0.0.1:5000/

## Características de la Aplicación

- **Página de Inicio**: Ver todos los anuncios en `/`
- **Ver Anuncio**: Ver un anuncio específico en `/ad/<slug>/`
- **Crear Anuncio**: Crear un nuevo anuncio en `/admin/ad/`
- **Registro de Usuario**: Registrar un nuevo usuario en `/signup/`

## Estructura del Proyecto

```
anuncios/
├── pyproject.toml    # Configuración del proyecto y dependencias
├── README.md         # Este archivo
└── src/
    └── anuncios/     # Código fuente de la aplicación
        ├── forms.py  # Definiciones de formularios
        ├── run.py    # Punto de entrada de la aplicación
        ├── static/   # Archivos estáticos (CSS, JS, etc.)
        └── templates/ # Plantillas HTML
            ├── admin/  # Plantillas de administración
            │   ├── ad_form.html     # Formulario de creación de anuncios
            │   └── signup_form.html # Formulario de registro de usuarios
            ├── ad_view.html         # Plantilla de vista de anuncios
            ├── base_template.html   # Plantilla base
            └── index.html           # Plantilla de página de inicio
```

## Modo Debugging

Para ejecutar la aplicación en modo de depuración, establece `FLASK_ENV=development` antes de ejecutar la aplicación.

```bash
# Alternativamente, cuando no se usa entorno virtual
flask run --debug
# o
flask --app src/anuncios/run.py run --debug
```