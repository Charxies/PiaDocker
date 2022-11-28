from django.shortcuts import render, redirect
from empleado.forms import EmpleadoForm
from empleado.models import Empleado


# Create your views here.
def emp(request: object) -> object:
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmpleadoForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    empleado = Empleado.objects.all()
    return render(request, "show.html", {'empleado': empleado})


def edit(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, 'edit.html', {'empleado': empleado})


def update(request, id):
    empleado = Empleado.objects.get(id=id)
    form = EmpleadoForm(request.POST,instance=empleado)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'empleado': empleado})


def destroy(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("/show")
