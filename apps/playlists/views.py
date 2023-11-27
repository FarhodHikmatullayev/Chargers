from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.playlists.models import Playlist
from apps.playlists.serializers import PlaylistSerializer
from apps.shared.pagination import CustomPagination


class PlaylistListCreateApiView(ListCreateAPIView):
    pagination_class = CustomPagination
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    permission_classes = (AllowAny,)


class PlaylistRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaylistSerializer
    queryset = Playlist.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'pk'
