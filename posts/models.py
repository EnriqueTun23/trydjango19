from django.db import models

# Create your models here.
#tablas

class Post(models.Model):
    titulo = models.CharField(max_length=120)#max_lenght = 120
    contenido = models.TextField()
    actualizado = models.DateTimeField(auto_now=True, auto_now_add=False)
    publicado = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'