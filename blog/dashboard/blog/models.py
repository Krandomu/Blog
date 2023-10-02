from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subcategories', blank=True)

    def __str__(self):
        return self.name

class Posts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='posts', blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Titulos(models.Model):
    contenido = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='titulos')

    def get_seccion_tipo(self):
        return 'titulo'

class Textos(models.Model):
    contenido = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='textos')

    def get_seccion_tipo(self):
        return 'texto'

class Codigos(models.Model):
    contenido = models.TextField(blank=True, null=True)
    lenguaje = models.CharField(max_length=100, blank=True, null=True)  # Agrega un campo para el lenguaje del código
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='codigos')

    def get_seccion_tipo(self):
        return 'codigo'

class Imagenes(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    archivo = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='imagenes')

    def get_seccion_tipo(self):
        return 'imagen'

class Archivos(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    archivo = models.FileField(upload_to='archivos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='archivos')

    def get_seccion_tipo(self):
        return 'archivo'
