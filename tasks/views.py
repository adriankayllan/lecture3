from django.shortcuts import render

tarefas = ["Ir ao mercado", "Ir a academia", "Estudar para a prova"]
def index(request):
    context = {"tarefas": tarefas}
    return render(request, "tasks/index.html", context)

def adicionar(request):
    return render(request, "tasks/adicionar.html")