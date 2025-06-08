# Tienda de Historias — Django Project (Coderhouse • Entrega 3)

_E-commerce y blog para una librería física & online._

---

## Tabla de contenidos
1. [Descripción](#descripción)
2. [Estructura de apps](#estructura-de-apps)
3. [Tecnologías](#tecnologías)
4. [Instalación rápida](#instalación-rápida)
5. [Uso](#uso)
6. [Flujo de permisos](#flujo-de-permisos)
7. [Capturas](#capturas)
8. [Autor](#autor)

---

## Descripción

**Tienda de Historias** es la tercera entrega de Coderhouse “Tu primera página web”.  
Incluye:

| Módulo | Funcionalidad |
|--------|---------------|
| **Core**  | Home, navbar Bootstrap, login/logout, mensajes flash. |
| **Product** | Catálogo público (cards) + CRUD completo para _staff_ (tabla con búsqueda). |
| **Client** | CRUD de clientes para _staff_ (tabla, búsqueda, formularios). |
| **Blog** | Publicaciones públicas (cards con búsqueda) + CRUD para _staff_ con imágenes y categorías. |

---

## Estructura de apps

```text
TiendaHistorias/
│
├── core/       # Página de inicio y navegación
│├── templates/core/index.html
│└── views.py
│
├── product/
│├── models.py          # Product, Category
│├── views.py           # CRUD + catálogo
│├── templates/product/
│└── forms.py
│
├── client/
│├── models.py          # Client
│├── views.py           # CRUD
│├── templates/client/
│└── forms.py
│
├── blog/
│├── models.py          # Post, Category
│├── views.py           # CRUD + list
│├── templates/blog/
│└── forms.py
│
├── static/             # CSS, imágenes (login, no-image)
└── templates/base.html # Layout Bootstrap común

Tecnologías
Python 3.13

Django 5.2

Bootstrap 5.3 (CDN)

SQLite 3 (dev)

Git / GitHub

Instalación rápida
# 1. Clonar el repo
git clone https://github.com/<usuario>/TiendaHistorias.git
cd TiendaHistorias

# 2. Crear y activar entorno
python -m venv .venv
source .venv/Scripts/activate   # Linux/macOS: source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Migraciones + usuario admin
python manage.py migrate
python manage.py createsuperuser

# 5. Cargar categorías demo (opcional, vía admin)
python manage.py runserver
# abrir http://127.0.0.1:8000/admin/

Uso
| URL                   | Rol       | Descripción                           |
| --------------------- | --------- | ------------------------------------- |
| `/`                   | Público   | Página de inicio.                     |
| `/accounts/login/`    | Público   | Inicio de sesión.                     |
| `/productos/`         | Público   | Catálogo de productos (con búsqueda). |
| `/clientes/clients/`  | **Staff** | CRUD de clientes.                     |
| `/productos/list/`    | **Staff** | CRUD de productos.                    |
| `/blog/posts/`        | Público   | Blog con buscador.                    |
| `/blog/posts/create/` | **Staff** | Crear post (imagen + categoría).      |

Nota: las vistas de gestión requieren usuarios con is_staff=True.

Flujo de permisos
Visitante: navega Home, Catálogo y Blog. Sin login.

Cliente: (futuro) usuario estándar; hoy solo vistas públicas.

Empleado (staff): accede a CRUD de Product, Client y Blog.

Autenticación gestionada con Django contrib.auth; las sesiones expiran al cerrar el navegador (SESSION_EXPIRE_AT_BROWSER_CLOSE = True).

Capturas
Home	Catálogo

(Añade tus screenshots en static/README/ y actualiza los nombres.)

Autor
Marisa Canale 
Proyecto desarrollado en el marco de Coderhouse — Python & Django 2025.


> ### Cómo usarlo
> 1. Graba el contenido como `README.md` en la raíz del proyecto.  
> 2. (Opcional) coloca un par de capturas en `static/README/` con los nombres usados en la sección de **Capturas** o ajusta los paths.  
> 3. `git add README.md static/README/*` y `git commit -m "Add full README"`.

