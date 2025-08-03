from django.contrib import admin
from .models import Category,post


# Register your models here.
@admin.register(post)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'fecha', 'activo', 'publicado', 'actualizado', 'categoria', 'imagen', 'contenido')
    
admin.site.register(Category)