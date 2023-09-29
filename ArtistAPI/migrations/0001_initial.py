# Generated by Django 4.2.3 on 2023-07-22 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=256)),
                ('work_type', models.CharField(choices=[('YT', 'Youtube'), ('IG', 'Instagram'), ('OT', 'Others')], default='YT', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('work', models.ManyToManyField(to='ArtistAPI.work')),
            ],
        ),
    ]