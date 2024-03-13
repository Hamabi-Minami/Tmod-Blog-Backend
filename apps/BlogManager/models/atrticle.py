from django.db import models
from apps.UserManager.models.user import UserModel
from apps.BlogManager.models.features import FeatureTypesModel


class ArticleModel(models.Model):
    topic = models.CharField(max_length=100)
    rates = models.IntegerField(default=10)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic, self.author

    class Meta:
        verbose_name = 'articles'
        verbose_name_plural = 'articles_table'


class FeaturesModel(models.Model):
    feature_type = models.ForeignKey(FeatureTypesModel, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.feature_type.name

    class Meta:
        verbose_name = 'features'
        verbose_name_plural = 'features_table'
