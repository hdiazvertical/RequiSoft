from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="acceso")
def crear(request):
    context = {}
    return render(request, 'actividades/crear.html', context)
