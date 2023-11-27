from django.urls import path

from apps.playlists.views import PlaylistListCreateApiView, PlaylistRetrieveUpdateDestroyAPIView

app_name = 'playlists'

urlpatterns = [
    path('list-create/', PlaylistListCreateApiView.as_view(), name='list_create'),
    path('<int:pk>/retrieve-update-destroy/', PlaylistRetrieveUpdateDestroyAPIView.as_view(), name='list_create'),
]
