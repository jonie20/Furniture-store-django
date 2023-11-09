from django.shortcuts import render
from django.http import HttpResponse
from .models import Shop

# Create your views here.

def home(request):
    return render(request,'index.html', {'navbar': 'home'} )


def shop(request):

    data = Shop.objects.all()
    return render(request, 'shop.html', {'navbar': 'shop', 'item':'item'})


def layout(request):
    return render(request, 'layout.html', {'navbar': ''})

def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})

def services(request):
    return render(request, 'services.html', {'navbar': 'services'})

def about(request):
    return render(request, 'about.html', {'navbar': 'about'})
    
def blog(request):
    return render(request, 'blog.html', {'navbar': 'blog'})

def checkout(request):
    return render(request, 'checkout.html')

def cart(request):
    return render(request, 'cart.html')