from django.http import HttpResponse
from django.shortcuts import render
from apps.usuario.models import usuario
from .forms import usuarioForm

# Create your views here.

    #return render(request,"index.html",{})
def contacto(request):
   
    return render(request, "contact.html", {})
 
def home_view(request):
    my_context = {
       "my_text": "This is about us"
    } 
    return render(request, "User/home.html", my_context)
def user_detail_view(request):
    obj = usuario.objects.get(id=1)
    context = {
        'objeto':obj
    }
    return render(request, "prueba_templates.html",{})
    
def user_create_view(request):
    form = usuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        'form':form
    }
    return render(request, "prueba_templates_create.html", {'form':form})

def login(request):
    return render(request, "login.html", {})