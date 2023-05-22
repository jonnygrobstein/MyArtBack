from .models import User, Artist, Artwork
from rest_framework import viewsets
from rest_framework import permissions
from .serializer import UserSerializer, ArtistSerializer, ArtworkSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [permissions.IsAuthenticated]
