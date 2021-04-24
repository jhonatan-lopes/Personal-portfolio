from django.db import models
from django.db.models.deletion import CASCADE
from main.models import MyInfo

class Publication(models.Model):
    """ Publication model.
    """
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

    title = models.CharField(
        max_length=200, 
        unique=True,
        verbose_name="Title")
    
    year = models.CharField(
        max_length=50, 
        verbose_name="Publishing Year",
    )

    authors = models.CharField(
        max_length=255,
        default="",
        verbose_name = "Authors",
        help_text = "Example: 'F. Author, J. Doe.'. A name can be highlighted by enclosing it in html 'strong' tags: <strong>J. Doe</strong>.", 
    )

    DEFAULT_MYINFO_ID = 1
    my_info = models.ForeignKey(
        MyInfo,
        on_delete=CASCADE,
        default=DEFAULT_MYINFO_ID)

    publisher = models.CharField(
        max_length=200, 
        default="",
        verbose_name="Publisher",
        help_text="Journal, publisher, patent provider, etc.")

    link = models.URLField(
        max_length=200,
        blank=True,
        verbose_name="External hyperlink",
        help_text="Redirects user to publication. (e.g. DOI for article)"
    )

    class Meta:
        ordering = ['kind','year', 'title']

    def authors_list(self):
        authors = self.authors.replace(
            self.my_info.my_initials,
            "<strong>"+self.my_info.my_initials+"</strong>")
        return authors

    def __str__(self):
        short_title = ' '.join(self.title.split(' ')[:5]) # Only four first words
        return f"{self.year}  - {short_title}"
    




