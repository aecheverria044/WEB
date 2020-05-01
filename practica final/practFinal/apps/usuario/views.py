from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def contacto(request,*args, **kwargs):
   return render(request,"contact.html",{})
def home_view(request,*args, **kwargs):
   print(args,kwargs)
   print(request.user)
   return render(request,"index.html",{})
