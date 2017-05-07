from django.contrib import admin

from music.models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
