from django.shortcuts import render
from catalogo.models import Juego
from django.core.paginator import Paginator
from django.db.models import Q

def buscar_juegos(request):
    query = request.GET.get('q', '')

    resultados = Juego.objects.filter(
        Q(nombre__icontains=query) | Q(plataforma__icontains=query)).order_by('id')
    
    paginator = Paginator(resultados, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    contexto = {
        'query': query,
        'lista_juegos': page_obj
    }

    return render(request, 'buscador/resultados_busqueda.html', contexto)