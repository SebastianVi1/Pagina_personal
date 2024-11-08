from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modificado")
    dinamic_url = models.URLField(verbose_name="URL", null=True, blank=True)
    name_url = models.CharField(max_length=100, verbose_name="Nombre url", null=True, blank=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"  
        ordering = ["-created"]
    
    def __str__(self):
        return self.title