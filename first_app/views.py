from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Now I am from views.py !"}
    return render(request,'first_app/index.html',context=my_dict)

def product(request):
    help_dict= {'help_insert':"Product Page"}
    return render(request,'first_app/product.html',context=help_dict)