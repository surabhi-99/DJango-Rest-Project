# Generated by Django 4.2.3 on 2023-07-22 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ArtistAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='work',
            new_name='works',
        ),
    ]
