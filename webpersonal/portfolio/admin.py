from django.contrib import admin
from .models import Project
# Register your models here.
class ProjectAdmin(admin.ModelAdmin): #activamos los campos de creado y modificado
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)