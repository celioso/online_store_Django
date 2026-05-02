from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from django.contrib import messages

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro completado correctamente")
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html',
                {'form':form})

'''def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('home')
        else:
            form = LoginForm()
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        print(form.errors)
        messages.error(request, 'usuarios/login.html', {'form': form})
'''
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST) # Recibe los datos
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, "Inicio de sesión correcto.")
            return redirect('home')
        else:
            # Si NO es válido, NO limpies el form. 
            # Deja que contenga los errores para que se muestren en el HTML.
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        # Aquí es cuando cargan la página por primera vez (GET)
        form = LoginForm() 

    # El render debe ir afuera de los IF para que siempre devuelva una respuesta
    return render(request, 'usuarios/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente")
    return redirect('login')

@login_required
def perfil_view(request):
    return render(request, 'usuarios/perfil.html')