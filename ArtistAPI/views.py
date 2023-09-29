from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, WorkSerializer, ArtistSerializer
from .models import Work, Artist


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({"detail": "not found"}, status=status.HTTP_404_NOT_FOUND)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def work(request):
    if request.method == 'POST':
        serializer = WorkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            for artist_id in request.data['artist_ids']:
                artist = Artist.objects.get(user=artist_id)
                artist.works.add(serializer.instance)

            return Response({"work": serializer.data})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.query_params.get('work_type'):
        works = Work.objects.filter(work_type=request.query_params.get('work_type'))
    elif request.query_params.get('artist'):
        artist = Artist.objects.filter(name=request.query_params.get('artist'))
        print(artist)
        works = Work.objects.filter(artist=artist.first())
    else:
        works = Work.objects.all()

    serializer = WorkSerializer(works, many=True)
    return Response({"work": serializer.data})
