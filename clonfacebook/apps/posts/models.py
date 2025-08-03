from django.db import models
from django.utils import timezone

# Create your models here.



#categorias

class Category(models.Model):
    name = models.CharField(max_length=30, null=False)
   
    def __str__(self):
        return self.name
    
#posts
class post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True) 
    fecha = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    publicado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    imagen= models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-publicado']
    def __str__(self):
            return self.titulo
       
    def delete(self, using=None, keep_parents=False):
            self.imagen.delete()
            super().delete(using=using, keep_parents=keep_parents)
           