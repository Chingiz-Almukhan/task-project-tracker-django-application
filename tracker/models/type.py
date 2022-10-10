from django.db import models


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
