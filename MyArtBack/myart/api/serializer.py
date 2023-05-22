from .models import User, Artist, Artwork
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['name', 'nationality', 'residence', 'yearofbirth', 'yearofdeath', 'styles', 'bio', 'image']

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['title', 'artist', 'year', 'medium', 'description', 'location', 'notes', 'image']

