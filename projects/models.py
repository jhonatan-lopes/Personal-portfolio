from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
import tagulous.models

# class KindTag(TagBase):
#     # ... fields here
#     pass

#     # ... methods (if any) here

# class TaggedKinds(GenericTaggedItemBase):
#     tag = models.ForeignKey(
#         KindTag,
#         on_delete=models.CASCADE,
#         related_name="%(app_label)s_%(class)s_items",
#     )


# class TechnologyTag(TagBase):
#     # ... fields here
#     pass

#     # ... methods (if any) here

# class TaggedTechnologies(GenericTaggedItemBase):
#     tag = models.ForeignKey(
#         TechnologyTag,
#         on_delete=models.CASCADE,
#         related_name="%(app_label)s_%(class)s_items",
#     )

# Create your models here.
class Project(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name="Title",
        unique=True
    )

    year = models.SmallIntegerField()

    hyperlink = models.URLField(
        blank=True,
        verbose_name="External hyperlink",
        help_text = "Redirects to project's external webpage."
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
