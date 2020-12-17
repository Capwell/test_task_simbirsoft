from django.db import models


class CreatedModel(models.Model):
    """Абстрактная модель. Добавляет дату создания."""
    created_on = models.DateTimeField(
        'Создано',
        auto_now_add=True
    )

    class Meta:
        abstract = True
