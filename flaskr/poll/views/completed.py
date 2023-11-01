from .blueprint import *

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