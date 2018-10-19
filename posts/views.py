from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import PostFormulario
from .models import Post


def posts_lista(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated:
        context = {
            "titulo": "Mi lista de usuario",
            "lista" : queryset
        }
        
    else:
        context = { 
            "titulo": "Lista"
        }
    return render(request, "index.html", context)
    

def posts_crear(request):
    form = PostFormulario(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/posts/')
    # if request.method == "POST":
    #     print request.POST["Titulo"]
        # Post.objects.create(Titulo)
    context = {
        "formulario": form
    }
    return render(request, "crear.html", context)

def posts_detalles(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    context = {
        "titulo": instance.titulo,
        "info" : instance
    }
    return render(request, "detalles.html", context)

def posts_actualizar(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    form = PostFormulario(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/posts/')

    context = {
        "titulo": instance.titulo,
        "instancia": instance,
        "formulario": form
    }
    return render(request, "crear.html", context)

def posts_eliminar(request, pk=None):
    instance = get_object_or_404(Post, pk=pk)
    instance.delete()
    # return redirect("posts:index")
    return HttpResponseRedirect('/posts/')