from rest_framework import serializers

from apps.playlists.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, required=False)
    created_time = serializers.DateTimeField(read_only=True, required=False)
    updated_time = serializers.DateTimeField(read_only=True, required=False)

    class Meta:
        model = Playlist
        fields = '__all__'
