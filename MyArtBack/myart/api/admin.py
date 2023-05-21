from django.contrib import admin
from .models import User, Artist, Artwork

# Register your models here.
admin.site.register({User, Artist, Artwork})