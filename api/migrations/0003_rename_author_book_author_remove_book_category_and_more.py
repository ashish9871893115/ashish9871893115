# Generated by Django 4.0.1 on 2022-04-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_book_isbn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='Author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.AddField(
            model_name='book',
            name='Category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='Name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]