from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "club/index.html")

def index_profe(request):
    return render(request, "club/index_profe.html")

def index_jugadores(request):
    return render(request, "club/index_jugadores.html")

def index_categoria(request):
    return render(request, "club/index_categoria.html")

def index_equipo(request):
    return render(request, "club/index_equipo.html")


def profe_create(request):
    if request.method == "POST":
        form = forms.ProfeForm(request.POST)
        if form.is_valid():
            profe = form.save(commit=False)
            form.save()
            return render(request,"club/index_profe.html")
    else:
        form = forms.ProfeForm()
    return render(request, "club/profe_create.html", {"form": form})


def profe_list(request):
    profes = models.Profe.objects.all()
    context = {"profes": profes}
    return render(request, "club/profe_list.html", context)


def profe_borrar(request, id):
    profe = models.Profe.objects.get(id=id)
    profe.delete()
    return redirect("club:profe_list")


def jugador_create(request):
    if request.method == "POST":
        form = forms.JugadorForm(request.POST)
        if form.is_valid():
            profe = form.save(commit=False)
            form.save()
            return render(request,"club/index.html")
    else:
        form = forms.JugadorForm()
    return render(request, "club/jugador_create.html", {"form": form})


def jugador_list(request):
    jugadores = models.Jugador.objects.all()
    context = {"jugadores": jugadores}
    return render(request, "club/jugador_list.html", context)


def jugador_borrar(request, id):
    jugador = models.Jugador.objects.get(id=id)
    jugador.delete()
    return redirect("club:jugador_list")


def categoria_create(request):
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save(commit=False)
            form.save()
            return render(request,"club/index.html")
    else:
        form = forms.CategoriaForm()
    return render(request, "club/categoria_create.html", {"form": form})


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "club/categoria_list.html", context)


def categoria_borrar(request, id):
    categoria = models.Categoria.objects.get(id=id)
    categoria.delete()
    return redirect("club:categoria_list")


def equipo_create(request):
    if request.method == "POST":
        form = forms.EquipoForm(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            form.save()
            return render(request,"club/index.html")
    else:
        form = forms.EquipoForm()
    return render(request, "club/equipo_create.html", {"form": form})


def equipo_list(request):
    equipos = models.Equipo.objects.all()
    context = {"equipos": equipos}
    return render(request, "club/equipo_list.html", context)


def equipo_borrar(request, id):
    equipo = models.Equipo.objects.get(id=id)
    equipo.delete()
    return redirect("club:equipo_list")


def equipo_jugador_create(request):
    if request.method == "POST":
        form = forms.EquipoJugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"club/index.html")
    else:
        form = forms.EquipoJugadorForm()
    return render(request, "club/equipo_jugador_create.html", {"form": form})


def equipo_jugador_list(request):
    equipo_jugadores = models.EquipoJugador.objects.all()
    context = {"equipo_jugadores": equipo_jugadores}
    return render(request, "club/equipo_jugador_list.html", context)


def equipo_jugador_borrar(request, id):
    equipo_jugador = models.EquipoJugador.objects.get(id=id)
    equipo_jugador.delete()
    return redirect("club:equipo_jugador_list")


def profe_editar(request, id):
    profe_aux = models.Profe.objects.get(id=id)
   
    if request.method == "POST":
        form = forms.ProfeForm(request.POST, instance=profe_aux)
        
        if form.is_valid():
            profe = form.save(commit=False)
            profe.save()
            return profe_list(request)
    else:
        form = forms.ProfeForm(instance=profe_aux)
        return render(request, "club/profe_edit.html", {"form": form, "profe_id": profe_aux.id})

    return profe_list(request)


def categoria_editar(request, id):
    categoria_aux = models.Categoria.objects.get(id=id)
    
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST, instance=categoria_aux)
        
        if form.is_valid():
            categoria = form.save(commit=False)
            categoria.save()
            return categoria_list(request)
    else:
        form = forms.CategoriaForm(instance=categoria_aux)
        return render(request, "club/categoria_edit.html", {"form": form, "categoria_id": categoria_aux.id})

    return categoria_list(request)

def equipo_editar(request, id):
    equipo_aux = models.Equipo.objects.get(id=id)
    
    if request.method == "POST":
        form = forms.EquipoForm(request.POST, instance=equipo_aux)
        
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.save()
            return equipo_list(request)
    else:
        form = forms.EquipoForm(instance=equipo_aux)
        return render(request, "club/equipo_edit.html", {"form": form, "equipo_id": equipo_aux.id})

    return equipo_list(request)

def equipo_jugador_editar(request, id):
    equipo_jugador_aux = models.EquipoJugador.objects.get(id=id)
    
    if request.method == "POST":
        form = forms.EquipoJugadorForm(request.POST, instance=equipo_jugador_aux)
        
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.save()
            return equipo_list(request)
    else:
        form = forms.EquipoJugadorForm(instance=equipo_jugador_aux)
        return render(request, "club/equipo_jugador_edit.html", {"form": form, "equipo_jugador_id": equipo_jugador_aux.id})

    return equipo_jugador_list(request)