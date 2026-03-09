from django.shortcuts import render, get_object_or_404
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
    
def detalle_juego(request, pk):
    juego = get_object_or_404(Juego, pk=pk)
    contexto = {'juego': juego}
    return render(request, 'catalogo/detalle_juego.html', contexto)