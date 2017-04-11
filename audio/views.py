# ~#~ coding: UTF-8 ~#~

u"""
En este archivo se encuentran las vistas de la aplicación.
"""

# Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from __future__ import unicode_literals
from flask import abort
from flask import flash
from flask import jsonify
from flask import render_template
from flask import request
from flask import session

from . import app
from .helpers import download_youtube_video
from .helpers import watson_process_audio
from .helpers import youtube_url_validation
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Views ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        isThereAnError = False

        if not request.form['video_url']:
            isThereAnError = True
            flash('¡Debe indicar la URL del video a procesar!')

        if not request.form['video_lan']:
            isThereAnError = True
            flash('¡Debe indicar el lenguaje a usar!')

        # Extract id to use in filename
        video_id = youtube_url_validation(request.form['video_url'])

        if not video_id:
            isThereAnError = True
            flash('¡La URL que introdujo no es válida!')

        session['video_id'] = video_id
        session['video_lan'] = request.form['video_lan']
        session['video_url'] = request.form['video_url']

        if not isThereAnError:
            return render_template("results.html")

    return render_template("input.html")


@app.route('/download-youtube-video', methods=['GET'])
def json_download_youtube_video():
    if not ('video_url' in session and session['video_url']):
        return abort(400)

    download_youtube_video(session['video_url'])

    return jsonify(message='OK')


@app.route('/watson-process-audio', methods=['GET'])
def json_watson_process_audio():
    if not ('video_id' in session and session['video_id']):
        return abort(400)

    if not ('video_lan' in session and session['video_lan']):
        return abort(400)

    return jsonify(
        message='OK',
        video_id=session['video_id'],
        **watson_process_audio(session['video_id'], session['video_lan'])
    )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
