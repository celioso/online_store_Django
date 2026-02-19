from django.shortcuts import render

def lista_juegos(request):
    juegos = [
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
    ]

    contexto_catalogo_juegos = {'lista_juegos': juegos}
    
    return render(request, 'catalogo/lista_juegos.html', contexto_catalogo_juegos)
    
