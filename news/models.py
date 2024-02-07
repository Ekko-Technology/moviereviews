from django.db import models

# Create your models here.
class News(models.Model):
    topic = models.CharField(max_length = 30)
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    link = models.URLField(blank=True)

    # __str__ is a special method within python that converts  objects into strings and only strings. or better readability when migrating models to admin interface
    def __str__(self):
        return self.headline