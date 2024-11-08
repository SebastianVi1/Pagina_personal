from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True) #Nos registra la fecha de creachion del modelo
    updated = models.DateTimeField(auto_now=True) #Registra la fecha y hora en que se modifico

    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["created"] #Indicamos que queremos que muestre primero los proyectos mas actuales

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name='Fecha de publicacion', default=timezone.now)
    image = models.ImageField(verbose_name='imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 