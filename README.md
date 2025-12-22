# tienda

## MVC

MVC significa **Model–View–Controller** y es un **patrón de arquitectura de software** muy utilizado para organizar aplicaciones, especialmente en **web, backend y aplicaciones de escritorio**. A continuación te lo explico de forma **clara, estructurada y práctica**, con un ejemplo en **Python**, alineado con tu perfil técnico.

## ¿Qué es MVC?

MVC separa una aplicación en **tres responsabilidades bien definidas**:

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
* Facilita **pruebas unitarias**
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
* El servidor responde con el HTML de esa página.

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