from django.db import models

# Create your models here.
class Publication(models.Model):
    authors = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    date_published = models.CharField(max_length=10)
    doi = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.authors}, {self.date_published}'

