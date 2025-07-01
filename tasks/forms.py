from django import forms

class NovaTarefaForm(forms.Form):
    tarefa = forms.CharField(label="Nova Tarefa: ")