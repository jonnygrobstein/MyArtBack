from django.urls import path #, include, re_path

from .views import UserViewSet, ArtistViewSet, ArtworkViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list'})),
    path('artist', ArtistViewSet.as_view({'get': 'list'})),
    path('artwork', ArtworkViewSet.as_view({'get': 'list'})),
]

# urlpatterns += [
#     re_path(r'^auth/', include('djoser.urls')),
# ]
