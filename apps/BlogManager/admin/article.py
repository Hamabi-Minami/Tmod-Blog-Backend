from django.contrib import admin
from apps.BlogManager.models.atrticle import ArticleModel


@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'topic',
        'rates',
        'created',
        'author',
    )
