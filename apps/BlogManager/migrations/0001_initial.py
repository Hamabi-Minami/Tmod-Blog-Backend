# Generated by Django 5.0.2 on 2024-03-08 23:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('rates', models.IntegerField(default=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserManager.usermodel')),
            ],
            options={
                'verbose_name': 'articles',
                'verbose_name_plural': 'articles_table',
            },
        ),
        migrations.CreateModel(
            name='FeaturesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('content', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BlogManager.articlemodel')),
            ],
            options={
                'verbose_name': 'features',
                'verbose_name_plural': 'features_table',
            },
        ),
    ]