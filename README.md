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
