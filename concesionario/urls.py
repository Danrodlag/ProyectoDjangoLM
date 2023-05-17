from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'), # Página home
    path('vertodos/', views.verTodos, name='verTodos'), # Listado de libros
    path('vertodos/nuevo/', views.nuevo, name='nuevo'), # Formulario para crear nuevo libro
    path('vertodos/coche/<int:id>/', views.verCoche, name='verCoche'), # Detalle de un libro
    path('vertodos/coche/actualizar/<int:id>/', views.actualizar, name='actualizar'),
    path('vertodos/coche/eliminar/<int:id>/', views.eliminar, name='eliminar'),
]
