# Tienda

## MVC

*MVC* significa **Model–View–Controller** y es un patrón de arquitectura de software muy utilizado para organizar aplicaciones, especialmente en web, backend y aplicaciones de escritorio. A continuación te lo explico de forma clara, estructurada y práctica, con un ejemplo en *Python*, alineado con tu perfil *técnico*.

## ¿Qué es MVC?

**MVC** separa una aplicación en **tres responsabilidades bien definidas**:

| Componente     | Responsabilidad                     |
| -------------- | ----------------------------------- |
| **Model**      | Lógica de negocio y datos           |
| **View**       | Presentación (lo que ve el usuario) |
| **Controller** | Intermediario entre Model y View    |

## 1. Model (Modelo)

* Representa los **datos**
* Contiene la **lógica de negocio**
* Accede a bases de datos o fuentes externas
* **No conoce** a la vista

### Ejemplo (Python)

```python
# model/user_model.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def is_valid_email(self):
        return "@" in self.email
```

## 2. View (Vista)

* Se encarga de la **presentación**
* No contiene lógica de negocio
* Solo muestra datos

### Ejemplo (consola)

```python
# view/user_view.py
def show_user(user):
    print(f"Nombre: {user.name}")
    print(f"Email: {user.email}")
```

## 3. Controller (Controlador)

* Recibe acciones del usuario
* Coordina Model y View
* Aplica reglas de negocio

### Ejemplo

```python
# controller/user_controller.py
from model.user_model import User
from view.user_view import show_user

def create_user(name, email):
    user = User(name, email)

    if not user.is_valid_email():
        print("Email inválido")
        return

    show_user(user)
```

## Flujo MVC

```
Usuario → Controller → Model
                   ↓
                 View → Usuario
```

## Estructura de carpetas recomendada

```text
project/
│
├── model/
│   └── user_model.py
│
├── view/
│   └── user_view.py
│
├── controller/
│   └── user_controller.py
│
└── main.py
```

```python
# main.py
from controller.user_controller import create_user

create_user("Mario", "mario@email.com")
```

## MVC en frameworks reales

| Framework       | Cómo aplica MVC           |
| --------------- | ------------------------- |
| **Django**      | MVT (Model–View–Template) |
| **Flask**       | MVC flexible              |
| **Spring Boot** | MVC clásico               |
| **ASP.NET**     | MVC estricto              |

## Ventajas de MVC

* Código más **ordenado y mantenible**
* Facilita *pruebas unitarias*
* Escalabilidad
* Separación clara de responsabilidades

## Cuándo usar MVC

* APIs REST
* Aplicaciones web
* Proyectos medianos y grandes
* Sistemas con reglas de negocio claras

## MVTU

**MVTU** no es un patrón de arquitectura estándar ampliamente reconocido como MVC o MVT. Normalmente, cuando se menciona **MVT** (sin la “U”), se hace referencia al patrón usado por **Django**: **Model–View–Template**. La “U” suele interpretarse, según el contexto, como **User** o **URL**, pero **no forma parte del patrón formal**.

Dado el uso más común, te explico **MVT (Model–View–Template)** y aclaro dónde encaja el **usuario (U)** o las **URLs**, que probablemente es lo que estás consultando.

## MVT (Model – View – Template)

### 1. Model

* Define los **datos** y la **lógica de negocio**
* Se conecta a la base de datos (ORM)

```python
# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

### 2. View

* Contiene la **lógica de aplicación**
* Procesa solicitudes HTTP
* Interactúa con el Model
* Devuelve una respuesta

```python
# views.py
from django.shortcuts import render
from .models import User

def user_list(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})
```

### 3. Template

* Define la **presentación (HTML)**
* No contiene lógica de negocio

```html
<!-- templates/users.html -->
<h1>Usuarios</h1>
<ul>
  {% for user in users %}
    <li>{{ user.name }} - {{ user.email }}</li>
  {% endfor %}
</ul>
```

## ¿Dónde entra la “U” (User o URL)?

### Opción más común: **URL Dispatcher**

En Django, las **URLs** actúan como el **controlador real** del patrón.

```python
# urls.py
from django.urls import path
from .views import user_list

urlpatterns = [
    path("users/", user_list),
]
```

📌 En términos arquitectónicos:

```
User → URL → View → Model
               ↓
            Template → User
```

Por eso algunos describen Django como:

> **MVT + URL dispatcher**

o informalmente **MVTU**.

## Comparación rápida MVC vs MVT

| MVC        | Django (MVT) |
| ---------- | ------------ |
| Controller | URL + View   |
| View       | Template     |
| Model      | Model        |

## Conclusión clara

* **MVTU no es un patrón oficial**
* En **Django**, el flujo real es:
  **User → URL → View → Model → Template**
* La “U” suele referirse al **Usuario** o al **enrutador de URLs**

# Codigos de respuesta HTTP

A continuación presento una **explicación clara y estructurada de HTTP**.

## ¿Qué es HTTP?

**HTTP** (*HyperText Transfer Protocol*) es el **protocolo de comunicación** que permite el intercambio de información entre un **cliente** (normalmente un navegador o una app) y un **servidor web**.

Es la base del funcionamiento de la **World Wide Web**.

## ¿Cómo funciona HTTP?

HTTP sigue un modelo **cliente–servidor** y opera mediante un esquema de **petición–respuesta**:

1. El **cliente** envía una **petición HTTP** al servidor.
2. El **servidor** procesa la petición.
3. El servidor devuelve una **respuesta HTTP** con datos o un resultado.

Ejemplo simple:

* El navegador solicita una página web.
* El servidor responde con el **HTML** de esa página.

## Métodos HTTP (Verbos)

Los métodos indican **qué acción** se desea realizar sobre un recurso:

| Método     | Uso principal                  |
| ---------- | ------------------------------ |
| **GET**    | Obtener información            |
| **POST**   | Enviar datos (crear)           |
| **PUT**    | Actualizar un recurso completo |
| **PATCH**  | Actualizar parcialmente        |
| **DELETE** | Eliminar un recurso            |

Ejemplo:

* `GET /usuarios` → obtener usuarios
* `POST /usuarios` → crear un usuario

## Códigos de estado HTTP

Indican el **resultado** de la petición:

### Respuestas comunes

* **200 OK** → Todo correcto
* **201 Created** → Recurso creado
* **400 Bad Request** → Error del cliente
* **401 Unauthorized** → No autorizado
* **404 Not Found** → Recurso no existe
* **500 Internal Server Error** → Error del servidor

## HTTP vs HTTPS

| HTTP         | HTTPS               |
| ------------ | ------------------- |
| No cifrado   | Cifrado con SSL/TLS |
| Menos seguro | Seguro              |
| Puerto 80    | Puerto 443          |

Actualmente, **HTTPS es el estándar obligatorio** para aplicaciones web modernas.

## Características importantes de HTTP

* **Sin estado (stateless)**: cada petición es independiente.
* Usa **headers** para enviar metadatos.
* Puede transportar **HTML, JSON, XML, imágenes, videos**, etc.
* Es la base de **APIs REST**.

## Ejemplo de petición HTTP

```
GET /api/usuarios HTTP/1.1
Host: ejemplo.com
Authorization: Bearer token
```

Respuesta:

```
HTTP/1.1 200 OK
Content-Type: application/json

[
  { "id": 1, "nombre": "Mario" }
]
```


## ¿Dónde se usa HTTP?

* Navegadores web
* APIs REST (Django, Node.js, AWS API Gateway)
* Aplicaciones móviles
* Microservicios y arquitecturas serverless

# Codigos de respuesta HTTP

A continuación presento una **explicación completa y ordenada de los códigos de respuesta HTTP**, tal como se usan en aplicaciones web y APIs REST.

## ¿Qué son los códigos de respuesta HTTP?

Los **códigos de respuesta HTTP** indican el **resultado de una solicitud** realizada por un cliente a un servidor.
Se agrupan por rangos numéricos, donde cada rango representa una categoría.

## Clasificación de los códigos HTTP

### **1xx – Respuestas informativas**

Indican que la solicitud fue recibida y está en proceso.

| Código                      | Significado                                   |
| --------------------------- | --------------------------------------------- |
| **100 Continue**            | El servidor recibió los encabezados, continúe |
| **101 Switching Protocols** | Cambio de protocolo                           |

Uso poco común en APIs REST.

### **2xx – Respuestas exitosas**

La solicitud fue procesada correctamente.

| Código             | Uso típico                             |
| ------------------ | -------------------------------------- |
| **200 OK**         | Solicitud exitosa                      |
| **201 Created**    | Recurso creado (POST)                  |
| **202 Accepted**   | Solicitud aceptada (proceso asíncrono) |
| **204 No Content** | Éxito sin contenido de respuesta       |

Ejemplo:

* `POST /usuarios` → **201 Created**
* `DELETE /usuarios/1` → **204 No Content**

### **3xx – Redirecciones**

Indican que el recurso cambió de ubicación.

| Código                    | Significado                   |
| ------------------------- | ----------------------------- |
| **301 Moved Permanently** | Redirección permanente        |
| **302 Found**             | Redirección temporal          |
| **304 Not Modified**      | Recurso no modificado (cache) |

Muy usados en navegación web y cacheo.

### **4xx – Errores del cliente**

La solicitud es incorrecta o no autorizada.

| Código                       | Uso                   |
| ---------------------------- | --------------------- |
| **400 Bad Request**          | Solicitud mal formada |
| **401 Unauthorized**         | No autenticado        |
| **403 Forbidden**            | Acceso prohibido      |
| **404 Not Found**            | Recurso no existe     |
| **405 Method Not Allowed**   | Método no permitido   |
| **409 Conflict**             | Conflicto de datos    |
| **422 Unprocessable Entity** | Error de validación   |

Ejemplo:

* Token inválido → **401**
* Falta un campo obligatorio → **422**

### **5xx – Errores del servidor**

El servidor falló al procesar una solicitud válida.

| Código                        | Uso                      |
| ----------------------------- | ------------------------ |
| **500 Internal Server Error** | Error genérico           |
| **502 Bad Gateway**           | Error entre servidores   |
| **503 Service Unavailable**   | Servicio caído           |
| **504 Gateway Timeout**       | Tiempo de espera agotado |

Común en microservicios y arquitecturas serverless.

## Códigos HTTP más usados en APIs REST

| Escenario           | Código recomendado |
| ------------------- | ------------------ |
| Obtener recurso     | 200                |
| Crear recurso       | 201                |
| Actualizar recurso  | 200 o 204          |
| Eliminar recurso    | 204                |
| Error de validación | 422                |
| No autenticado      | 401                |
| No autorizado       | 403                |
| Recurso inexistente | 404                |
| Error interno       | 500                |

## Buenas prácticas

* Use **códigos correctos**, no solo 200 para todo.
* Combine códigos HTTP con **mensajes claros en JSON**.
* En APIs, los 4xx deben explicar **qué hizo mal el cliente**.
* Reserve los 5xx solo para errores del servidor.

## Ejemplo de respuesta de error (API REST)

```json
{
  "error": "Email inválido",
  "code": 422
}
```

# Metodos http

A continuación presento una **explicación clara, completa y práctica de los métodos HTTP**, enfocada en su uso real en aplicaciones web y **APIs REST**.

## ¿Qué son los métodos HTTP?

Los **métodos HTTP** (también llamados *verbos HTTP*) indican **qué acción** desea realizar el cliente sobre un **recurso** del servidor.

Un recurso suele representarse por una URL, por ejemplo:

```
/usuarios
/usuarios/123
```

## Métodos HTTP principales

### **GET**

**Obtiene información** de un recurso.

* No modifica datos
* Es idempotente
* Puede ser cacheado

Ejemplo:

```
GET /usuarios
GET /usuarios/123
```

Código típico: **200 OK**

### **POST**

**Crea un nuevo recurso** o ejecuta una acción.

* Envía datos al servidor
* No es idempotente

Ejemplo:

```
POST /usuarios
```

Código típico: **201 Created**

### **PUT**

**Actualiza un recurso completo**.

* Reemplaza toda la información
* Es idempotente

Ejemplo:

```
PUT /usuarios/123
```

Código típico: **200 OK** o **204 No Content**

### **PATCH**

**Actualiza parcialmente** un recurso.

* Solo cambia algunos campos
* Es idempotente (en la práctica)

Ejemplo:

```
PATCH /usuarios/123
```

Código típico: **200 OK**

### **DELETE**

**Elimina un recurso**.

* Es idempotente

Ejemplo:

```
DELETE /usuarios/123
```

Código típico: **204 No Content**

## Métodos HTTP secundarios

| Método      | Uso                            |
| ----------- | ------------------------------ |
| **HEAD**    | Igual que GET, pero sin cuerpo |
| **OPTIONS** | Métodos permitidos (CORS)      |
| **TRACE**   | Diagnóstico                    |
| **CONNECT** | Túneles HTTPS                  |

En APIs REST normalmente se usan **GET, POST, PUT, PATCH y DELETE**.

## Idempotencia (concepto clave)

Un método es **idempotente** si ejecutarlo varias veces produce el **mismo resultado**:

| Método | Idempotente       |
| ------ | ----------------- |
| GET    | Sí                |
| PUT    | Sí                |
| PATCH  | Sí (generalmente) |
| DELETE | Sí                |
| POST   | No                |

## Relación método + acción (REST)

| Acción CRUD | Método HTTP |
| ----------- | ----------- |
| Crear       | POST        |
| Leer        | GET         |
| Actualizar  | PUT / PATCH |
| Eliminar    | DELETE      |

## Buenas prácticas en APIs REST

* No usar **GET** para modificar datos
* Usar **POST** para crear recursos
* Diferenciar **PUT vs PATCH**
* Responder con **códigos HTTP correctos**
* Usar **nombres de recursos en plural**

Ejemplo correcto:

```
POST /usuarios
GET /usuarios/123
DELETE /usuarios/123
```

## Ejemplo de uso real (API)

Solicitud:

```
PATCH /usuarios/123
```

Respuesta:

```json
{
  "id": 123,
  "nombre": "Mario",
  "activo": true
}
```

[httpdebugger](https://www.httpdebugger.com/tools/viewhttpheaders.aspx)

# Estructura de directorios

A continuación presento una **explicación clara y paso a paso de cómo se crea el “árbol” (estructura de directorios) de un proyecto Django**, desde cero.

## 1. Crear el entorno virtual (recomendado)

Antes de crear el proyecto, se aísla el entorno de Python:

```bash
python -m venv venv
```

Activar:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux / macOS**

```bash
source venv/bin/activate
```

## 2. Instalar Django

Con el entorno virtual activo:

```bash
pip install django
```

## 3. Crear el proyecto Django

Este comando **crea el árbol inicial del proyecto**:

```bash
django-admin startproject tienda_videojuegos
```

Estructura generada:

```
tienda_videojuegos/
├── manage.py
└── tienda_videojuegos/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## 4. Explicación del árbol inicial

### `manage.py`

* Punto de entrada del proyecto
* Ejecuta comandos como `runserver`, `migrate`, `createsuperuser`

### Carpeta del proyecto (`tienda_videojuegos/` interna)

> Esta carpeta tiene el mismo nombre del proyecto, pero **contiene la configuración principal**.

#### `settings.py`

* Configuración global del proyecto
* Apps, base de datos, idioma, zona horaria

#### `urls.py`

* Enrutador principal de URLs

#### `wsgi.py`

* Configuración para servidores tradicionales (Gunicorn, uWSGI)

#### `asgi.py`

* Configuración para aplicaciones asíncronas (WebSockets)

#### `__init__.py`

* Indica que es un paquete Python

## 5. Crear una aplicación Django

Dentro del proyecto, se crean **apps** para separar funcionalidades:

```bash
python manage.py startapp productos
```

Nuevo árbol:

```
productos/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
    └── __init__.py
```

## 6. Relación proyecto vs aplicación

| Proyecto              | Aplicación               |
| --------------------- | ------------------------ |
| Configuración general | Funcionalidad específica |
| URLs principales      | Lógica de negocio        |
| Base de datos         | Modelos                  |

Ejemplo:

* Proyecto: `tienda_videojuegos`
* Apps: `productos`, `usuarios`, `pedidos`

## 7. Árbol típico de un proyecto Django real

```
tienda_videojuegos/
├── venv/
├── manage.py
├── tienda_videojuegos/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── productos/
├── usuarios/
├── templates/
├── static/
└── requirements.txt
```

## 8. Buenas prácticas

* Usar **entorno virtual**
* Separar funcionalidades en apps
* Mantener `settings.py` organizado
* Crear carpetas `templates/` y `static/`


agragar bootstrap 

 link [https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css](https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css)

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css">
```

Ejemplo de promp para que chatgpt me genere el bloque

**ejemplo**

Quiero que me ges el codigo html para un bloque content de django Para un formulario de contacto que tenga campo nombre completo, direccion de correo electronico, telefono y el mensaje de contacto

Devera tener un boton para enviar y un titulo arriba que ponge contactenos, con un subtitulo de color gris, con letras mas pequeñas que ponga mensaje relacionado.

Los estilos deben ser de **bootstrap**(ya tengo la hoja enlazada, de modo que no me la porporciones) y debe ser completamente responsiva.

codigo que me genero

```html
{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-12 col-md-8 col-lg-6">

            <h2 class="text-center mb-1">Contáctenos</h2>
            <p class="text-center text-muted mb-4">mensaje relacionado</p>

            <form method="post">
                {% csrf_token %}

                <div class="mb-3">
                    <label for="nombre" class="form-label">Nombre completo</label>
                    <input type="text" class="form-control" id="nombre" name="nombre" required>
                </div>

                <div class="mb-3">
                    <label for="email" class="form-label">Correo electrónico</label>
                    <input type="email" class="form-control" id="email" name="email" required>
                </div>

                <div class="mb-3">
                    <label for="telefono" class="form-label">Teléfono</label>
                    <input type="tel" class="form-control" id="telefono" name="telefono">
                </div>

                <div class="mb-3">
                    <label for="mensaje" class="form-label">Mensaje</label>
                    <textarea class="form-control" id="mensaje" name="mensaje" rows="4" required></textarea>
                </div>

                <div class="d-grid">
                    <button type="submit" class="btn btn-primary">
                        Enviar mensaje
                    </button>
                </div>
            </form>

        </div>
    </div>
</div>
{% endblock content %}
```

[fontawesome](https://fontawesome.com/search)

# <header>

En HTML, **`<header>`** es una **etiqueta semántica** que se utiliza para definir el **encabezado** de una página web o de una sección específica.

### ¿Para qué sirve `<header>`?

Se usa para agrupar contenido introductorio o de navegación, como:

* Logotipo o nombre del sitio
* Títulos (`<h1>` a `<h6>`)
* Menús de navegación
* Iconos o botones principales

### Ejemplo básico

```html
<header>
  <h1>Mi sitio web</h1>
  <nav>
    <a href="#">Inicio</a>
    <a href="#">Servicios</a>
    <a href="#">Contacto</a>
  </nav>
</header>
```

### Características importantes

* Puede existir **más de un `<header>`** en una página.
* Puede estar dentro de:

  * `<body>`
  * `<section>`
  * `<article>`
* **No** debe colocarse dentro de `<footer>`, `<address>` u otro `<header>`.

### Diferencia con `<head>`

| `<head>`        | `<header>`            |
| --------------- | --------------------- |
| Metadatos       | Contenido visible     |
| No visible      | Visible al usuario    |
| Título, CSS, JS | Títulos, menús, logos |

### Ventajas

* Mejora la **accesibilidad**
* Mejora el **SEO**
* Hace el código más claro y **mantenible**

### Para cargar los datos en Shell de Django utilizando ChatGPT

se le escribe a **ChatGPT**

Dame un codigo para el shell de Django que introduzca los siguientes datos en el modelo Juego.

´´´python 
{'nombre': 'Dogo Racing', 'precio': 29.99, 'plataforma':'PC, PS5, Xbox Serie X'}, 
{'nombre': 'PLatform', 'precio': 14.99, 'plataforma':'PC, Switch'},
{'nombre': 'Urban Darkness', 'precio': 39.99, 'plataforma':'PC, PS5'}, 
{'nombre': 'Highspeeed', 'precio': 29.99, 'plataforma':'PC, Xbox Serie X'}, 
{'nombre': 'Night Mode', 'precio': 19.99, 'plataforma':'PC, pS4, Xbox One'}, 
{'nombre': 'The Grand Thief', 'precio': 59.99, 'plataforma':'PC, PS5, Xbox Serie X'}, 
{'nombre': 'Sunset Vibe', 'precio': 24.99, 'plataforma':'PC, Switch, Mobile'}, 
{'nombre': 'Dark Whispers', 'precio': 34.99, 'plataforma':'PC, PS5, Xbox Serie X'}, 
{'nombre': 'Space Zero', 'precio': 44.99, 'plataforma':'PC, PS5'}, 
{'nombre': 'Resident Evil', 'precio': 85.99, 'plataforma':'PS5'}, 
{'nombre': 'Mario Bros', 'precio': 25.99, 'plataforma':'Switch'}, 
{'nombre': 'Terminator', 'precio': 25.9, 'plataforma':'PC'},
´´´

Este esa el modelo y la APP se llama catalogo

´´´python
from django.db import models

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    plataforma = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
´´´

y megenera este código 

´´´python
from catalogo.models import Juego

juegos = [
    {'nombre': 'Dogo Racing', 'precio': 29.99, 'plataforma':'PC, PS5, Xbox Serie X'},
    {'nombre': 'PLatform', 'precio': 14.99, 'plataforma':'PC, Switch'},
    {'nombre': 'Urban Darkness', 'precio': 39.99, 'plataforma':'PC, PS5'},
    {'nombre': 'Highspeeed', 'precio': 29.99, 'plataforma':'PC, Xbox Serie X'},
    {'nombre': 'Night Mode', 'precio': 19.99, 'plataforma':'PC, PS4, Xbox One'},
    {'nombre': 'The Grand Thief', 'precio': 59.99, 'plataforma':'PC, PS5, Xbox Serie X'},
    {'nombre': 'Sunset Vibe', 'precio': 24.99, 'plataforma':'PC, Switch, Mobile'},
    {'nombre': 'Dark Whispers', 'precio': 34.99, 'plataforma':'PC, PS5, Xbox Serie X'},
    {'nombre': 'Space Zero', 'precio': 44.99, 'plataforma':'PC, PS5'},
    {'nombre': 'Resident Evil', 'precio': 85.99, 'plataforma':'PS5'},
    {'nombre': 'Mario Bros', 'precio': 25.99, 'plataforma':'Switch'},
    {'nombre': 'Terminator', 'precio': 25.90, 'plataforma':'PC'},
]

for juego in juegos:
    Juego.objects.create(**juego)

print("Juegos insertados correctamente.")
´´´

## Creacion de superUsuario

´´´shell
python manage.py createsuperuser
Nombre de usuario (leave blank to use 'juan'): 
Dirección de correo electrónico: falso@hotmail.com
Password: 
Password (again):
Superuser created successfully.
´´´

Esto crea el super usuario y para ingresar se coloca `host/doc` en el *navegador*, se tiene que ingresar el usuario y la contraseña que se creó. 
