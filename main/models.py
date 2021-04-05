from django.db import models


class Education(models.Model):

    title = models.CharField(
        max_length=100,
        default="",
        help_text="Example: PhD in Engineering Science",
    )

    start_date = models.PositiveSmallIntegerField(
        default=2020,
    )

    end_date = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    institution = models.CharField(
        max_length=100,
        default="",
        help_text="Example: University of Oxford, UK",
    )

    hyperlink = models.URLField(
        blank=True
    )

    class Meta:
        verbose_name = "degree"

    def __str__(self):
        return f"{self.title}"



class Expertise(models.Model):

    title = models.CharField(
        max_length=100,
        default="",
        help_text="Example: Data Science and Visualisation",
    )

    description = models.CharField(
        max_length=255,
        default="",
        help_text="Example: Analysis libraries: pandas, numpy",
    )

    def __str__(self):
        return f"{self.title}"



class Experience(models.Model):

    title = models.CharField(
        max_length=100,
        default="",
        help_text="Example: Postdoctoral researcher",
    )

    start_date = models.PositiveSmallIntegerField(
        default=2020,
    )

    end_date = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
    )

    company = models.CharField(
        max_length=100,
        default="",
        help_text="Example: University of Oxford, UK",
    )

    hyperlink = models.URLField(
        blank=True
    )

    def __str__(self):
        return f"{self.title}"