from django.contrib import admin

from apps.playlists.models import Playlist


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'playlist_id', 'title', 'created_time')
    readonly_fields = ('id', 'created_time', 'updated_time')
