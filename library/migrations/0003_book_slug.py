# Generated by Django 3.2.16 on 2022-11-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20221104_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
