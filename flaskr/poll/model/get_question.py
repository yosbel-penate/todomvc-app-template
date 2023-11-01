from flaskr.db import get_db
from werkzeug.exceptions import abort
from flask import (g)


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