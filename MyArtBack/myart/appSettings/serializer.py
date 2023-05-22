from .models import Settings
from rest_framework import serializers


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = ['name', 'values']