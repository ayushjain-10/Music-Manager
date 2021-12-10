from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.db import get_db

bp = Blueprint('music', __name__)


@bp.route('/')
def index():
    search_term = request.args.get('search_term', None)
    query_param = request.args.get('query_param', None)

    db = get_db()
    if search_term is None or query_param is None:
        posts = db.execute(
            'SELECT *'
            ' FROM song'
            ' ORDER BY title'
        ).fetchall()
    else:
        posts = db.execute(
            "SELECT * FROM song WHERE {} LIKE '%{}%' ORDER BY title".format(
                query_param, search_term)
        ).fetchall()
    return render_template('music/index.html', posts=posts)


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']
        song_url = request.form['song_url']

        error = None

        if not title or not artist or not album or not song_url :
            error = 'Field is empty'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO song (title, artist, album, song_url)'
                ' VALUES (?, ?, ?, ?)',
                (title, artist, album, song_url)
            )
            db.commit()
            return redirect(url_for('music.index'))

    return render_template('music/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT *'
        ' FROM song'
        ' WHERE id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return post


@bp.route('/<int:id>/play', methods=('GET', 'POST'))
def update(id):
    post = get_post(id)

    return render_template('music/play.html', post=post)



@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM song WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('music.index'))