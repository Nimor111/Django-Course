from __future__ import absolute_import, unicode_literals

from pytube import YouTube

from celery import shared_task
from celery import chain

from django.conf import settings
from music.models import Song

from subprocess import call

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

import os


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
    return 'mp3/{}.mp3'.format(filename.split('/')[1])


@shared_task
def send_email(filename, email):
    mail = EmailMultiAlternatives(
        subject="{}".format(filename),
        body="Here's your song mateio.",
        from_email="Youtube downloader <youtube_downloader@hotmail.com>",
        to=["{}".format(email)],
        reply_to=["georgi.bojinov@hotmail.com"],
    )
    mail.template_id = 'c00b4864-3192-4650-9ca4-e83772f929d3'

    mail.attach_alternative(
        "<p>Here's your song!</p>", "text/html"
    )

    with open('{}'.format(filename), 'rb') as file:
        mail.attachments = [
            ('{}'.format(filename), file.read(), 'application/mp3')
        ]

    mail.send()


@shared_task
def chain_tasks(url, email):
    return chain(download_url.s(url), convert_mp4.s(), send_email.s(email))
