from .blueprint import *

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