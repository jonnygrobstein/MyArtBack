from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet, ArtistViewSet, ArtworkViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('artist/', ArtistViewSet.as_view({'get': 'list'})),
    path('artwork/', ArtworkViewSet.as_view({'get': 'list'})),
    path('register/', UserViewSet.as_view({'post': 'create'})),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


