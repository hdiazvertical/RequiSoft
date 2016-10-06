from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from forms import ActividadesForm
from django.contrib import messages
from django.shortcuts import redirect

@login_required(login_url="acceso")
def crear(request):
    form = ActividadesForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit = False)
        instance.usuario = request.user
        instance.save()
        return redirect('resultado')

        # Clean form
        #form = ActividadesForm()
        # Success message
        #messages.success(request, 'Actividad registrada satisfactoriamente')

    context = {
        'form' : form
    }
    return render(request, 'actividades/crear.html', context)

def resultado(request):
    messages.success(request, 'Actividad registrada satisfactoriamente')
    return render(request, "actividades/resultado.html", {})
