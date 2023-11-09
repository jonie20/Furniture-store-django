from django.contrib import admin

from .models import Shop
from .models import Teachers

# Register your models here.
admin.site.register(Shop)
admin.site.register(Teachers)