from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id',
                    '__str__',
                    'created_on',
                    'author',
                    )
    readonly_fields = ('author', )
