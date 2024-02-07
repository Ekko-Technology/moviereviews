# to add models into the admin interface 
from django.contrib import admin
from .models import Movie, Review

# modifies admin interface 
class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ['date'] #specify which field u want to display as readonly within the admin

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review, ReviewAdmin)