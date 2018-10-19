from django.contrib import admin

# Register your models here.
# Esto se crea para poder teneer un buen panel administrativo
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["titulo", "publicado"]
    list_display_links = ["publicado"]
    list_filter = ["publicado", "actualizado"]
    search_fields = ["titulo"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)