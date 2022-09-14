from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, './Home/vistas/home.html')

def cafe(request):

    cafe = [{'name': 'Capuccino', 'img': 'capuccino.jpg', 'valor': 3000 ,'descripcion': 'El capuccino es cafe compuesto por expreso de café y leche con espuma de leche'},
                {'name': 'Café Americano', 'img': 'cafe.webp', 'valor': 2500, 'descripcion': 'El Café americano consta de cafe más agua'},
                {'name': 'Latte', 'img': 'latte.jpg', 'valor': 2000, 'descripcion': 'El late es un hermano del capuccino pero mas vistoso, por su corte entre el cafe y la leche'},
                {'name': 'Moca', 'img': 'moca.jpg', 'valor': 3500, 'descripcion': 'El café moca es un capuccino con chocolate'},
                {'name': 'Expreso', 'img': 'expreso.webp', 'valor': 1500, 'descripcion': 'El Expreso es un corto de café concentrado'},
             ]

    return render(request, './Home/vistas/cafe.html', {
        'cafe': cafe
    })

def pasteles(request):

    pasteles = [{'nombre': 'Tres leches', 'img':'tres.jpg', 'valor': 3000, 'descripcion':'Trozo de torta tres leches'},
                {'nombre': 'Mil hojas', 'img':'mil.jpg', 'valor': 3000, 'descripcion':'Trozo de torta mil hojas'},
                {'nombre': 'Chocolate', 'img':'chocolate.jpg', 'valor': 3000, 'descripcion':'Trozo de torta de chocolate'},
                ]
    return render(request, './Home/vistas/pasteles.html', {
        'pasteles': pasteles
    })

def artesanales(request):

    helados = [{'name': 'Chocolate', 'img':'chocolate.jpg', 'valor': 8000, 'descripcion':'Helado de sabor chocolate artesanal'},
                {'name': 'Limon', 'img':'limon.jpg', 'valor': 8000, 'descripcion':'Helado de sabor limon artesanal'},
                {'name': 'Vainilla', 'img':'vainilla.jpg', 'valor': 8000, 'descripcion':'Helado de sabor vainilla artesanal'},
    ]
    return render(request, './Home/vistas/artesanales.html', {'helados': helados})

def marcas(request):
    return render(request, './Home/vistas/marcas.html')