from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('poll', __name__)

@bp.route('/')
def poll():
    db = get_db()
    questions = ...
    if g.user:
        questions = db.execute(
            'SELECT q.id, body, is_checked, author_id, username'
            ' FROM question q JOIN user u ON q.author_id = u.id'
            ' WHERE u.id = ?'
            ' ORDER BY created DESC',
            ( g.user['id'],)
        ).fetchall()
    else:
        questions = db.execute(
            'SELECT q.id, body, is_checked, author_id, username'
            ' FROM question q JOIN user u ON q.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
    filter='all'
    return render_template('poll/index.html', questions=questions, filter=filter)

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
            is_checked = 0
            db = get_db()
            db.execute(
                'INSERT INTO question ( body, is_checked, author_id)'
                ' VALUES (?, ?, ?)',
                ( body, is_checked, g.user['id'])
            )
            db.commit()
            return redirect(url_for('index'))

    return render_template('poll/index.html')

def get_question(id, check_author=True):
    question = get_db().execute(
        'SELECT q.id, body, created, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' WHERE q.id = ?',
        (id,)
    ).fetchone()

    if question is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and question['author_id'] != g.user['id']:
        abort(403)

    return question

@bp.route('/poll/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_question(id)
    db = get_db()
    db.execute('DELETE FROM question WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))

@bp.route('/poll/update', methods=['POST'])
@login_required
def update():
    if request.method == 'POST':
        id = int(request.json['question_id'])
        is_checked = int(request.json['is_checked'])
        db = get_db()
        db.execute(
            'UPDATE question SET is_checked = ?'
            ' WHERE id = ?',
            ( is_checked, id)
        )
        db.commit()
        return {'question_id': id, 'is_checked': is_checked, 'status': 'update'}

@bp.route('/poll/clearcomplete')
@login_required
def clear_complete():
    db = get_db()
    db.execute('DELETE FROM question WHERE author_id = ?', (g.user['id'],))
    db.commit()
    return redirect(url_for('index'))

@bp.route('/poll/active')
def active():
    db = get_db()
    questions = db.execute(
        'SELECT q.id, body, is_checked, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' WHERE is_checked = 1'
        ' ORDER BY created DESC'
    ).fetchall()
    filter = 'active'
    return render_template('poll/index.html', questions=questions, filter=filter)

@bp.route('/poll/completed')
def completed():
    db = get_db()
    questions = db.execute(
        'SELECT q.id, body, is_checked, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' WHERE is_checked = 0'
        ' ORDER BY created DESC'
    ).fetchall()
    filter='completed'
    return render_template('poll/index.html', questions=questions, filter=filter )