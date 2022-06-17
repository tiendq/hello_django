# Generated by Django 4.0.5 on 2022-06-17 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_article_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Article slug'),
            preserve_default=False,
        ),
    ]