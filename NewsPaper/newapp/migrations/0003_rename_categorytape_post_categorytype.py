# Generated by Django 4.2.4 on 2023-08-06 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_rename_autoruser_author_authoruser_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categoryTape',
            new_name='categoryType',
        ),
    ]
