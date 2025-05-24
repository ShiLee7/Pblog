# blog/models.py

from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.utils import timezone
from django.utils.text import slugify
from parler.utils.context import switch_language


from parler.utils.context import switch_language

class Tag(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=30, unique=True),
        slug=models.SlugField(max_length=30, unique=True, blank=True),
    )

    def save(self, *args, **kwargs):
        # Set the slug for the current language if not provided
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)

class Article(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200),
        content=models.TextField(),
        slug=models.SlugField(max_length=200, blank=True, unique=False),
        # You can add summary, etc., here.
    )
    published_date = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100, default="ShiLee")
    tags = models.ManyToManyField(Tag, related_name="articles", blank=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article_detail', kwargs={'pk': self.pk})
