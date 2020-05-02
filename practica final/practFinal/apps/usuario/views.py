from django.http import HttpResponse
from django.shortcuts import render
from .models import usuario
# Create your views here.


def product_detail_view(request):
    obj = usuario.objects.get(id=1)
    context={
    'nombre': obj.nombre
    }
    return render(request,"index.html",{})
def contacto(request,*args, **kwargs):
   return render(request,"contact.html",{})
def home_view(request,*args, **kwargs):
   my_context={
       "my_text": "This is about us"
   } 
   return render(request,"index.html",my_context)
