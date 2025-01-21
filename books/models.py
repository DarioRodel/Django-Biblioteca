
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date= models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    publish_date = models.DateField()
    summary = models.TextField()
    def __str__(self):
        return f"{self.title}"
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
