from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = 'Postres disponibles'
    desserts_list = [
        {
            'nombre': 'flan de coco',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de vainilla',
            'descripcion': 'flan de vainilla',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de chocolate',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de queso',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de coco',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de coco',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
        {
            'nombre': 'flan de coco',
            'descripcion': 'flan de coco con caramelo',
            'img': 'flan_coco.jpg'
        },
            
    ]
    
    
    # desserts =[ 'flan de coco', 'flan de vainilla', 'flan de queso', 'flan de chocolate', 'flan de cafe', 'flan de fresa', 'flan de guayaba', 'flan de piña', 'flan de naranja', 'flan de limon','torta chocolate','total fresa']
    
    context ={'desserts_list': desserts_list, 'title': title}
    return render(request, 'index.html', context)

def about(request):
    title = 'About'
    content = 'informacion de la pagina nosotros'
    
    context ={ 'title': title, 'content': content }
    return render(request, 'about.html', context)

def contact(request):
    title = 'contact'
    content = 'informacion de la pagina de contacto'
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')
