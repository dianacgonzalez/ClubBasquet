from django.urls import path

from . import views

app_name = "club"

urlpatterns = [
    path("", views.index, name="index"),
    path("index/profe/", views.index_profe, name="index_profe"),
    path("index/jugadores/", views.index_jugadores, name="index_jugadores"),
    path("index/equipo/", views.index_equipo, name="index_equipo"),
    path("profe/create/", views.profe_create, name="profe_create"),
    path("profe/list", views.profe_list, name="profe_list"),
    path("profe/borrar/<int:id>/", views.profe_borrar, name="profe_borrar"),
    path("profe/editar/<int:id>/", views.profe_editar, name="profe_editar"),
    path("jugador/create/", views.jugador_create, name="jugador_create"),
    path("jugador/list", views.jugador_list, name="jugador_list"),
    path("jugador/editar/<int:id>/", views.jugador_editar, name="jugador_editar"),
    path("jugador/borrar/<int:id>/", views.jugador_borrar, name="jugador_borrar"),
     path("index/categoria/", views.index_categoria, name="index_categoria"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    path("categoria/list", views.categoria_list, name="categoria_list"),
    path("categoria/borrar/<int:id>/", views.categoria_borrar, name="categoria_borrar"),
    path("categoria/editar/<int:id>/", views.categoria_editar, name="categoria_editar"),
    path("equipo/create/", views.equipo_create, name="equipo_create"),
    path("equipo/list", views.equipo_list, name="equipo_list"),
    path("equipo/borrar/<int:id>/", views.equipo_borrar, name="equipo_borrar"),
    path("equipo/editar/<int:id>/", views.equipo_editar, name="equipo_editar"),
    path("equipo_jugador/create/", views.equipo_jugador_create, name="equipo_jugador_create"),
    path("equipo_jugador/list", views.equipo_jugador_list, name="equipo_jugador_list"),
    path("equipo_jugador/borrar/<int:id>/", views.equipo_jugador_borrar, name="equipo_jugador_borrar"),
    path("equipo_jugador/editar/<int:id>/", views.equipo_jugador_editar, name="equipo_jugador_editar"),
]
