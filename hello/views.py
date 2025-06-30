from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def adrian(request):
    return HttpResponse("<h1>Hello, Adrian!</h1>")

def saudacao(request, nome):
    return render(request, "hello/saudacao.html", {"nome": nome.capitalize()})