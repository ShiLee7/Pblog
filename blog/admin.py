# blog/admin.py

from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Article, Tag

admin.site.register(Article, TranslatableAdmin)

admin.site.register(Tag, TranslatableAdmin)