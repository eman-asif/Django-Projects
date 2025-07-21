from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class BookQuerySet(models.QuerySet):
    def recent(self):
        return self.filter(published_year__gte=2000)

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = BookQuerySet.as_manager()
