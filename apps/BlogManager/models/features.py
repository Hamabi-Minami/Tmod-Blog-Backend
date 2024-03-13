from django.db import models


class FeatureTypesModel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'feature_types'
        verbose_name_plural = 'feature_types_table'
