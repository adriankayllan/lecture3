from django.shortcuts import render
import datetime

def index(request):
    agora = datetime.datetime.now()
    context = {
        "newyaear": agora.month == 1 and agora.day == 1
    }
    return render(request, "newyear/index.html", context)