from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Hashtag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='hashtags', blank=True)

    def __str__(self):
        return self.name
