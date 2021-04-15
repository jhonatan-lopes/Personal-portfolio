from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
import tagulous.models
from publications.models import MyInfo


class Post(models.Model):

    title = models.CharField(
        max_length=100,
        default="",
        verbose_name="Title"
    )

    slug = models.SlugField(
        null=False,
        unique=True,
    )

    posted_by = models.ForeignKey(
        MyInfo,
        on_delete=models.CASCADE
    )

    date_posted = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    tags = tagulous.models.TagField(
        case_sensitive = False,
        space_delimiter = False,
    )

    thumbnail = models.ImageField(
        default = "Default_blogpost_thumbnail.png",
        upload_to = "Blog thumbnails",
    )

    banner = models.ImageField(
        default = "Default_project_banner.png",
        upload_to = "Blog banners",
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
            return (", ".join(tag.name for tag in tags[:5]) +
                     f" and {n_tags_left} others")
    
    def tags_list(self):
        return self.get_tags_string(self.tags.all())

    def __str__(self):
        short_title = self.title[:50]
        return f"{self.date_posted.year} - {short_title}"
    
    def get_absolute_url(self):
        return reverse("posts-detail", 
                        kwargs={
                            "year": self.date_posted.year,
                            "month": self.date_posted.month,
                            "slug": self.slug})
    
