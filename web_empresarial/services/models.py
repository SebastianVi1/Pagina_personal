from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen', upload_to='Services')
    created = models.DateTimeField(auto_now_add=True) #Nos registra la fecha de creachion del modelo
    updated = models.DateTimeField(auto_now=True) #Registra la fecha y hora en que se modifico

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["created"] #Indicamos que queremos que muestre primero los proyectos mas actuales

    def __str__(self):
        return self.title