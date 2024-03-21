from django.db import models


class UserModel(models.Model):
    GENDER_MAN = 'man'
    GENDER_WOMEN = 'women'
    GENDER_OTHER = 'other'

    choices = (
        ('man', 'man'),
        ('women', 'women'),
        ('other', 'other')
    )

    name = models.CharField(max_length=20)
    account = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=25)
    gender = models.CharField(choices=choices, max_length=20)
    email = models.EmailField(max_length=54, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'users'
        verbose_name_plural = 'users_table'
