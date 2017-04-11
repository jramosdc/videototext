# ~#~ coding: UTF-8 ~#~

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from __future__ import unicode_literals
import os
import re

from celery import Celery
import requests
import youtube_dl

from . import app
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Constants ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
YDL_OPTS = {
    'format': 'bestaudio/best',
    'audioformat': 'wav',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192',
    }]
}

YOUTUBE_REGEX = (
    r'(https?://)?(www\.)?'
    r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
    r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Setup ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
celery = Celery(app.name)
celery.conf.update(app.config)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# @celery.task
def download_youtube_video(video_url):
    ydl_opts = {
        'outtmpl': os.path.join(app.config['TEMP_DIRECTORY'], '%(id)s.%(ext)s')
    }

    ydl_opts.update(YDL_OPTS)

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(video_url, download=True)


# @celery.task
def watson_process_audio(video_id, video_lan):
    filename = os.path.join(
        app.config['TEMP_DIRECTORY'], '{}.wav'.format(video_id)
    )

    request_url = '{url}{language}_BroadbandModel'.format(
        url=app.config['WATSON_URL'], language=video_lan
    )

    response = requests.post(
        url=request_url,
        data=open(filename, 'rb'),
        headers={'Content-Type': 'audio/wav'},
        auth=(app.config['WATSON_USER'], app.config['WATSON_PASSWORD']),
    )

    os.remove(filename)

    return response.json()


# @celery.task
def youtube_url_validation(url):
    """Extract video id from youtube url."""

    youtube_regex_match = re.match(YOUTUBE_REGEX, url)

    if youtube_regex_match:
        return youtube_regex_match.group(6)

    return None
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
