from django.contrib import admin

from music.models import Song


# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass
