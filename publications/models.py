from django.db import models



# Create your models here.
class Publication(models.Model):
    authors = models.ManyToManyField("Author", related_name="publications")
    title = models.CharField(max_length=200, unique=True)
    # The year is stored as an integer without any checks.
    # It is up to the admin to put sensible year values in the field
    year = models.IntegerField()
    link = models.CharField(max_length=200, default="#")
    TYPE_CHOICES = [
        ('BK','Book'),
        ('AR', 'Article'),
        ('CF','Conference Paper'),
        ('BC', 'Book Chapter')
    ]
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='AR')
    journal = models.CharField(max_length=200, default="")

    def __str__(self):
        author_names = ''.join(author.name + ', ' for author in self.authors.all())
        return author_names + str(self.year)
    
    def get_author_names(self):
        return ''.join(author.name + ', ' for author in self.authors.all())

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


