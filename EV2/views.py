from django.shortcuts import render

def main(request):
    return render(request,'templatesProductos/main.html')

def mazerunner(request):
    data={
        "titulo":"maze runner",
        'Informacion':"Maze Runner es una trilogía de películas de ciencia ficción, acción y aventura, basadas en la saga de novelas, The Maze Runner, escritas por el autor de EE. UU., James Dashner..",
        'Publicacion':"19 de septiembre de 2014",
        'actores':"Dylan O'Brien, Thomas Brodie-Sangster, Kaya Scodelario",
        'imagen':'imagenes/maze.jpg'
       }
    return render(request,'templatesProductos/main.html',data)

def rapidoyfuriosos(request):
    data={
        "titulo":"Rapidos y furiosos",
        'Informacion':"Fast & Furious es una franquicia de medios estadounidense centrada en una serie de películas de acción que se ocupan en gran medida de automóviles.",
        'Publicacion':"22 de junio de 2001",
        'actores':"Vin Diesel, Michelle Rodriguez, Paul Walker"
        'imagen':'imagenes/rapido.jpg'
       }
    return render(request,'templatesProductos/main.html',data)

def planetadeltesoro(request):
    data={
        "titulo":"El planeta del tesero",
        'Informacion':"Jim Hawkins, un chico rebelde a quien siempre le han apasionado las historias de piratas, compite para encontrar un tesoro en el espacio exterior.",
        'Publicacion':"27 de noviembre de 2002 ",
        'actores':"Joseph Gordon-Levitt, Martin Short, Brian Murray"
        'imagen':'imagenes/tesoro.jpg'
       }
    return render(request,'templatesProductos/main.html',data)
