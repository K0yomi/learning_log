from django.contrib import admin
from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic) #Указывает на то, что управление моделью должно осуществляться через административный сайт.
admin.site.register(Entry)
