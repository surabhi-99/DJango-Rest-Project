from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Work, Artist


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['username', 'password']


class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Artist
        fields = ['name', 'works', 'user']
        extra_kwargs = {'works': {'required': False}}


class WorkSerializer(serializers.ModelSerializer):
    artists = ArtistSerializer(many=True, read_only=True)

    class Meta(object):
        model = Work
        fields = ['link', 'work_type', 'artists']

    def to_representation(self, instance):
        representation = super(WorkSerializer, self).to_representation(instance)
        representation['artists'] = ArtistSerializer(instance.artists.all(), many=True).data
        return representation
