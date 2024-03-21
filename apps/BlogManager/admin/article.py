from django.contrib import admin

from apps.BlogManager.api.blog_api import BlogSerializer
from apps.BlogManager.models.atrticle import ArticleModel


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'topic',
        'introduction',
        'rates',
        'created',
        'author',
    )
