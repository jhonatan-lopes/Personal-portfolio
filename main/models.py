from django.db import models

class MyInfo(models.Model):
    my_initials = models.CharField(
        default="",
        max_length=50,
        verbose_name="My Initials",
        help_text="Example: J Doe",
    )
    email = models.EmailField(
        default="",
        help_text="Email recipient for 'contact me' form"
    )
    profile_pic = models.ImageField(
        default = "Default_profile_pic.png",
        upload_to = "Profile_pics",
        help_text = "Picture displayed at home page"
    )
    cv = models.FileField(
        upload_to="CV",
        help_text = "Resume/CV to be made available for download at about page"
    )

    class Meta:
        verbose_name = "My Info"
        verbose_name_plural = "My Info"

    def __str__(self):
        return f"{self.my_initials}"

    def save(self, *args, **kwargs):
        self.pk = 1
        super(MyInfo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

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