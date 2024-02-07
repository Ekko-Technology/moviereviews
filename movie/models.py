# models, something like tables in SQL, are Python classes that represent database tables but unlike Flask, it does not require developers to write SQL queries into the db. 
# Migrations allow us to generate a database schema based on our model code. When a model is created/changed, new migrations should be created . To do so, run "python manage.py makemigrations" in the terminal followed by "python manage.py migrate" to apply the changes into the database schema
from django.db import models
# to establish the presence of a user and his level of authorization
from django.contrib.auth.models import User

# Create your models here.
# each model is a class that extends django.db.models.Model whilst each model attribute represents a database column
class Movie(models.Model):
    # CharField type is used for small to large string sizes. for large amount of text, use TextField
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    # blank=True makes this field optional
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
# creating a database/model for users to publish reviews
    
class Review(models.Model):
    text = models.TextField(max_length=200)
    # makes the datetime non-editable
    date = models.DateTimeField(auto_now_add=True)
    # Foreign key allows for a many-to-one relationship by linking existing model's primary keys with it, which here, allows users to post multiple reviews under the same identity
    # on_delete is a mandatory parameter when using foreign keys as they ensure all reviews associated to the user gets deleted when user is removed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # boolean field to ask if user will watch again
    watchAgain = models.BooleanField()

    def __str__(self):
        return self.text
