from django.shortcuts import render
from django.core.paginator import Paginator
from catalogo.models import Juego

def lista_juegos(request):
    '''juegos = Juego.objects.all()
    contexto_catalogo_juegos = {'lista_juegos': juegos}
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)'''

    juegos = Juego.objects.all().order_by('id')
    paginator = Paginator(juegos, 6)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    contexto_catalogo_juegos = {'lista_juegos': page_obj}
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)
    
