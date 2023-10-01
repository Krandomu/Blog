from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subcategorie', blank=True)

    def __str__(self):
        return self.name

class Posts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subcategorie = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='posts', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Titulos(models.Model):
    contenido = models.CharField(max_length=255)
    color = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='titulo')


class Textos(models.Model):
    contenido = models.TextField()
    color = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='texto')


class Codigos(models.Model):
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='codigo')


class Imagenes(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.ImageField(upload_to='imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='imagen')


class Archivos(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='archivos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='archivo')


