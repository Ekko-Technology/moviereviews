from django.contrib import admin
from .models import News

# Register your models here.
# this is the interface that transfer information from this IDE to the web's admin interface
admin.site.register(News)