# Generated by Django 4.0.1 on 2022-04-06 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_book_author_remove_book_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
    ]
