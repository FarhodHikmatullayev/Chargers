from django.db import models

from apps.shared.models import BaseModel


class Playlist(BaseModel):
    playlist_id = models.IntegerField()
    title = models.CharField(max_length=221)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to='playlists/')

    def __str__(self):
        return self.title
