# Tienda de Historias — Django Project (Coderhouse • Entrega 3)

_E‑commerce y blog para una librería física & online._

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

**Tienda de Historias** implementa:

| Módulo | Funcionalidad |
|--------|---------------|
| **Core**    | Home, navbar, login/logout, mensajes flash. |
| **Product** | Catálogo público (+ búsqueda) y CRUD de productos para empleados. |
| **Client**  | CRUD de clientes para empleados. |
| **Blog**    | Blog público + cualquier usuario autenticado puede crear posts; empleados pueden editar/eliminar. |

---

## Estructura de apps

```text
## Estructura de apps

TiendaHistorias/  
│  
├── core/                     # Página de inicio y navegación  
│   ├── templates/  
│   │   └── core/  
│   │       ├── base.html     # Layout Bootstrap común  
│   │       └── index.html    # Home  
│   └── views.py  
│  
├── product/  
│   ├── models.py             # Product, Category  
│   ├── views.py              # CRUD + catálogo  
│   ├── forms.py  
│   └── templates/  
│       └── product/  
│           └── …  
│  
├── client/  
│   ├── models.py             # Client  
│   ├── views.py              # CRUD  
│   ├── forms.py  
│   └── templates/  
│       └── client/  
│           └── …  
│  
├── blog/  
│   ├── models.py             # Post, Category  
│   ├── views.py              # CRUD + listado  
│   ├── forms.py  
│   └── templates/  
│       └── blog/  
│           └── …  
│  
├── static/                   # CSS, imágenes (login, no-image) 
```

---

## Tecnologías
Django 5.2 · Python 3.13 · Bootstrap 5.3

---

## Instalación rápida

```bash
git clone https://github.com/canalmar/TuPrimeraPaginaCanale.git
cd TuPrimeraPaginaCanale
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Uso

| URL | Descripción |
|-----|-------------|
| `/` | Home |
| `/productos/` | Catálogo público |
| `/blog/posts/` | Blog público |
| `/blog/posts/create/` | Crear post (login requerido) |
| `/productos/list/` | CRUD productos (staff) |
| `/clientes/clients/` | CRUD clientes (staff) |


## Flujo de permisos

| Rol | Acceso |
|-----|--------|
| Visitante | Home, Catálogo, Blog |
| Usuario autenticado | + Crear nuevo post |
| Empleado (`is_staff`) | + Gestión productos, clientes, editar / eliminar cualquier post |

Sesiones expiran al cerrar el navegador.

---

## Capturas
_Añade imágenes en `static/README/`._

---

## Autor
**Marisa Canale** – Coderhouse Python & Django 2025
