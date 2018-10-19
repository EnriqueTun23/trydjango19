from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_lista, name="index"),
    path('crear/', views.posts_crear),
    path('<int:pk>/', views.posts_detalles, name="detalle"),
    path('<int:pk>/actualizar/', views.posts_actualizar),
    path('<int:pk>/eliminar/', views.posts_eliminar)
]