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

    def get_author_names(self):
        return ', '.join(author.get_abbreviated_name() for author in self.authors.all())

    def __str__(self):
        author_names = self.get_author_names()
        short_title = ' '.join(self.title.split(' ')[:5]) # Only four first words
        return f"{author_names}, {self.year}  - {short_title}"
    
    

class Author(models.Model):
    last_name = models.CharField(max_length=200)
    given_names = models.CharField(max_length=200)
    email = models.EmailField()
    institution = models.CharField(max_length=200)

    def get_given_names_initials(self):
        given_names = self.given_names.strip(" .,!?#%^&*$£\"\'<>\\/{}[]@;:~`¬|<> ").split(" ")
        initials = ""
        for name in given_names:
            if name[0].isupper():
                initials += name[0] + "."
        return initials

    def get_abbreviated_name(self):
        return f"{self.last_name},  {self.get_given_names_initials()}"

    def __str__(self):
        return f"{self.get_abbreviated_name()} - {self.institution}"


