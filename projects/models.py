from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import tagulous.models


class Project(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        unique=True
    )

    slug = models.SlugField(
        null=False,
        unique=True,
    )

    year = models.CharField(
        max_length=255,
    )

    categories = tagulous.models.TagField(
        case_sensitive = False,
        space_delimiter = False,
        max_count = 3
    )

    technologies = tagulous.models.TagField(
        case_sensitive = False,
        space_delimiter = False
    )

    priority = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Display Priority",
        help_text = "An integer that represents a priority for displaying the project. A value of 1 will be displayed higher than a value of 2."
    )

    thumbnail = models.ImageField(
        default = "Default_project_thumbnail.svg",
        upload_to = "ProjectThumbnails",
    )

    banner = models.ImageField(
        default = "Default_project_banner.svg",
        upload_to = "ProjectBanners",
    )

    hyperlink = models.URLField(
        blank=True,
        verbose_name="External hyperlink",
        help_text = "Redirects to project's external webpage."
    )

    content = MarkdownxField()

    @property
    def formatted_content(self):
        "Render markdown to be displayed in template"
        return markdownify(self.content)

    @staticmethod
    def get_tags_string(tags):
        n_tags = len(tags)
        if n_tags <= 5:
            return ", ".join(tag.name for tag in tags)
        else:
            n_tags_left = n_tags - 5
            return (", ".join(tag.name for tag in tags[:5]) + f" and {n_tags_left} others")

    def categories_list(self):
        return self.get_tags_string(self.categories.all())
    
    def technologies_list(self):
        return self.get_tags_string(self.technologies.all())

    def __str__(self):
        short_title = self.title[:50]
        return f"{self.year} - {short_title}"
    
    def get_absolute_url(self):
        return reverse("projects-detail", 
                        kwargs={
                            "slug": self.slug})
    
