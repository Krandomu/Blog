from django.contrib import admin
from .models import Categories, SubCategories, Posts

# Register your models here.
admin.site.register(Categories)
admin.site.register(SubCategories)
admin.site.register(Posts)
