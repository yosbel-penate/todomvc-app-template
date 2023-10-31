from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('poll', __name__)

@bp.route('/poll')
def poll():
    db = get_db()
    questions = db.execute(
        'SELECT q.id, body, is_checked, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('poll/index.html', questions=questions)

@bp.route('/poll/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        body = request.form['body']
        error = None

        if not body:
            error = 'Question body is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO questions ( body, author_id)'
                ' VALUES (?, ?, ?)',
                ( body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('poll.index'))

    return render_template('poll/index.html')

def get_question(id, check_author=True):
    post = get_db().execute(
        'SELECT q.id, body, created, author_id, username'
        ' FROM question q JOIN user u ON p.author_id = u.id'
        ' WHERE q.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/poll/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_question(id)
    db = get_db()
    db.execute('DELETE FROM question WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('poll.index'))