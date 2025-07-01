from django.shortcuts import render, redirect
from django import forms
from .forms import NovaTarefaForm

def index(request):
    if "tarefas" not in request.session:
        request.session["tarefas"] = []

    context = {"tarefas": request.session["tarefas"]}
    return render(request, "tasks/index.html", context)

def adicionar(request):
    form = NovaTarefaForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            tarefa = form.cleaned_data["tarefa"]
            request.session["tarefas"] += [tarefa]
            return redirect('tasks:index')
        else:
            return render(request, "tasks/adicionar.html", context)
         
    context = {"form": form}
    return render(request, "tasks/adicionar.html", context)