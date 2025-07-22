from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
