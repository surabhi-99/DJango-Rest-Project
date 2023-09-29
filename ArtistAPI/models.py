from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

WORK_TYPES = [
    ('YT', 'Youtube'),
    ('IG', 'Instagram'),
    ('OT', 'Others')
]


class Work(models.Model):
    link = models.CharField(max_length=256)
    work_type = models.CharField(
        max_length=2,
        choices=WORK_TYPES,
        default='YT',
    )


class Artist(models.Model):
    name = models.CharField(max_length=256)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    works = models.ManyToManyField('Work', related_name='artists', blank=True)


@receiver(post_save, sender=User)
def create_artist(sender, instance, created, **kwargs):
    print("Creating Artist")
    if created:
        artist = Artist.objects.create(user=instance, name=instance.username)
        artist.save()
        instance.artist.save()
