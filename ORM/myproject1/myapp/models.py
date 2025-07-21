from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Profile(models.Model):  # One-to-One
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    biography = models.TextField()

class BookQuerySet(models.QuerySet):
    def recent(self):
        return self.filter(published_year__gte=2000)

class Book(models.Model):  # One-to-Many (ForeignKey to Author)
    title = models.CharField(max_length=100)
    published_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    objects = BookQuerySet.as_manager()

class Store(models.Model):  # Many-to-Many with Book
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)