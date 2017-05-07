from __future__ import absolute_import, unicode_literals

from pytube import YouTube

from celery import shared_task
from celery import chain

from django.conf import settings
from music.models import Song

from subprocess import call


@shared_task
def download_url(url):
    yt = YouTube(url)
    yt.set_filename(yt.filename.split()[0])
    video = yt.get('mp4', '720p')
    video.download(settings.MEDIA_ROOT)
    return 'media/{}'.format(yt.filename)


@shared_task
def convert_mp4(filename):
    call(['./command.sh', '{}.mp4'.format(filename), 'mp3/{}.mp3'.format(filename.split('/')[1])])


@shared_task
def chain_tasks(url):
    chain(download_url.s(url), convert_mp4.s())
