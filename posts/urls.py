from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_lista, name="index"),
    path('crear/', views.posts_crear),
    path('detalle', views.posts_detalles),
    path('actualizar', views.posts_actualizar),
    path('eliminar', views.posts_eliminar)
]