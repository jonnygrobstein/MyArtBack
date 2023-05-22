from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Settings

# Create your views here.
class SettingsView(APIView):
    def get(self, request, format=None):
        settingsDict = {}

        try:
            settingsObjects = Settings.objects.all()

            for settings in settingsObjects:
                settingsDict[settings.name] = settings.value

            return Response(settingsDict, status=200)
    
        except:
            return Response(status=404)
        
    def post(self, request, format=None):

        # This view we are going to create new settings in the DB

        #JSON Object: {"setings": [{"NAME":NAME, "VALUE":VALUE}, {"NAME":NAME, "VALUE":VALUE}]}
        settings = request.data['settings']
        bad_settings = []
        for setting in settings:
            try:
                new_setting = Settings(name=setting['NAME'], value=setting['VALUE'])
                new_setting.save()
            except:
                bad_settings.append(setting)

        if len(bad_settings) > 0:
            return Response({"INVALID SETTINGS": bad_settings}, status=200)

        else:
            return Response(status=200)
