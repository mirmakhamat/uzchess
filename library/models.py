from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='icons/')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    publication_date = models.IntegerField()
    page_size = models.IntegerField()
    image = models.FileField(upload_to='images/')
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    rating = models.FloatField()

    def __str__(self):
        return self.title
