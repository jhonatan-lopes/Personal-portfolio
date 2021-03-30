from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.deletion import CASCADE


class Publication(models.Model):
    """ Publication model.
    """
    authors = models.CharField(
        max_length=255,
        default="",
        verbose_name = "Authors",
        help_text = "Example: 'F. Author, J. Doe.'. A name can be highlighted with html tags: <strong>J. Doe</strong>.", 
        )
    title = models.CharField(
        max_length=200, 
        unique=True,
        verbose_name="Title")
    # The year is stored as an integer without any checks.
    # It is up to the admin to put sensible year values in the field
    year = models.IntegerField(
        verbose_name="Publishing Year",
    )
    link = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="External hyperlink",
        help_text="Redirects user to publication. (e.g. DOI for article)"
    )
    BOOK = "BK"
    ARTICLE = "AR"
    CONFERENCE_PAPER = "CF"
    BOOK_CHAPTER = "BC"
    PATENT = "PT"
    TYPE_CHOICES = [
        (BOOK,'Book'),
        (ARTICLE, 'Article'),
        (CONFERENCE_PAPER,'Conference Paper'),
        (BOOK_CHAPTER, 'Book Chapter'),
        (PATENT, 'Patent')
    ]
    kind = models.CharField(
        max_length=2,
        choices=TYPE_CHOICES,
        default='AR',
        verbose_name="Publication type")
    publisher = models.CharField(
        max_length=200, 
        default="",
        verbose_name="Publisher",
        help_text="Journal, publisher, patent provider, etc.")

    class Meta:
        ordering = ['kind','year', 'title']

    def get_author_names(self):
        return ', '.join(author.get_abbreviated_name() for author in self.authors.all())

    def __str__(self):
        short_title = ' '.join(self.title.split(' ')[:5]) # Only four first words
        return f"{self.year}  - {short_title}"
    

# class Author(models.Model):
#     """ Author model.
#     """
#     last_name = models.CharField(
#         max_length=200,
#         verbose_name="Last name",
#         help_text = "Author's last name (e.g. Newton)"
#     )
#     given_names = models.CharField(
#         max_length=200,
#         verbose_name="Given names",
#         help_text="Author's given names to be abbreviated (e.g. Isaac)"
#     )
#     email = models.EmailField(blank=True)
#     institution = models.CharField(max_length=200,
#         blank=True,
#         verbose_name="Institution",
#         help_text = "Current institution that author is a member of"
#     )

#     class Meta:
#         unique_together = ["last_name", "given_names"]

#     @property
#     def initials(self):
#         given_names = self.given_names.strip(" .,!?#%^&*$£\"\'<>\\/{}[]@;:~`¬|<> ").split(" ")
#         initials = ""
#         for name in given_names:
#             if name[0].isupper():
#                 initials += name[0] + "."
#         return initials

#     @property
#     def abbreviated_name(self):
#         return f"{self.initials} {self.last_name}"

#     def __str__(self):
#         return f"{self.abbreviated_name} - {self.institution}"

# class Owner(Author):
#     """ Owner model.
#         Child of Author. Only one owner is allowed.
#     """
#     def save(self, *args, **kwargs):
#         if not self.pk and Owner.objects.exists():
#             raise ValidationError("Only one owner istance is allowed!")
#         return super(Owner, self).save(*args, **kwargs)

# class PublicationAuthor(models.Model):
#     """ PublicationAuthor model.
#         Through table for handling Publication and Author relationship.
#         Makes sure that the order of authors in a publication is preserved.
#     """
#     publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     order = models.IntegerField()

#     class Meta:
#         ordering = ['publication','order',]
#         unique_together = ['author', 'publication', 'order']
#         verbose_name = "Publication's Author"
#         verbose_name_plural = "Publication's Authors"
    
#     def __str__(self):
#         return f"{self.publication} - Author {self.order} - {self.author.get_abbreviated_name()}"



