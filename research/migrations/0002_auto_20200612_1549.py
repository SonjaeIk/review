# Generated by Django 2.0.13 on 2020-06-12 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
    ]
