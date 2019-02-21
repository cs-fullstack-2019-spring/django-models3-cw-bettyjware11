from django.db import models

# Create your models here.
class Books(models.Model):
    books_name = models.CharField(max_length=200)
    books_pageNumber = models.IntegerField()
    books_genre = models.CharField(max_length=200)
    books_publishDate = models.DateField('date published')

    def __str__(self):
        return self.books_name

    # def __str__(self):
    #     return self.books_pageNumber
    # def __str__(self):
    #     return self.books_genre
    # def __str__(self):
    #     return self.books_publishDate


class Cars(models.Model):
    cars_make = models.CharField(max_length=20)
    cars_model = models.CharField(max_length=20)
    cars_year = models.IntegerField()

    def __str__(self):
        return self.cars_make
