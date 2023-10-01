from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='subcategorie', blank=True)

    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=100, unique=True)
    subcategorie = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='posts', blank=True)

    def __str__(self):
        return self.name
