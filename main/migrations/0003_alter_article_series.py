# Generated by Django 4.0.5 on 2022-06-17 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_article_options_article_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='series',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.articleseries', verbose_name='Series'),
        ),
    ]
