from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title = 'Postres disponibles'
    desserts =[ 'flan de coco', 'flan de vainilla', 'flan de queso', 'flan de chocolate', 'flan de cafe', 'flan de fresa', 'flan de guayaba', 'flan de piña', 'flan de naranja', 'flan de limon']
    
    context ={'desserts': desserts, 'title': title}
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
