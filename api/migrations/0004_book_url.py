# Generated by Django 3.1.5 on 2021-01-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210127_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.URLField(default='-'),
            preserve_default=False,
        ),
    ]
