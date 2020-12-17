from html import unescape

from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import strip_tags
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import get_current_authenticated_user

from core.models import CreatedModel


def validate_not_empty(value):
    if strip_tags(unescape(value)).isspace():
        raise ValidationError('Заметка не может быть пустой.')
    return value


class ArticleManager(models.Manager):
    def articles_by_author(self):
        return (
            self.get_queryset()
            .select_related('author')
            .filter(author=get_current_authenticated_user())
        )

    def articles_by_author_count(self):
        if get_current_authenticated_user():
            return self.articles_by_author().count()


class Article(CreatedModel):
    text = RichTextField(
        'Заметка',
        validators=[validate_not_empty, ],
    )
    author = CurrentUserField(verbose_name='Автор')

    objects = ArticleManager()

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        ordering = ['-created_on', ]

    def __str__(self):
        return strip_tags(unescape(self.text[:100]))
