# Generated by Django 3.1.5 on 2021-01-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_book_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='book',
            name='url',
        ),
    ]
