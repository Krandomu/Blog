from django.contrib import admin
from .models import Categories, SubCategories, Posts, Titulos, Textos, Codigos, Imagenes, Archivos

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Posts)
admin.site.register(Titulos)
admin.site.register(Textos)
admin.site.register(Codigos)
admin.site.register(Imagenes)
admin.site.register(Archivos)
