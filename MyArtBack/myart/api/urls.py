from django.urls import path

from .views import TestViewSet, UserViewSet, ArtistViewSet, ArtworkViewSet
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', TestViewSet.as_view({'get': 'list'})),
    path('artist', ArtistViewSet.as_view({'get': 'list'})),
    path('artwork', ArtworkViewSet.as_view({'get': 'list'})),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
