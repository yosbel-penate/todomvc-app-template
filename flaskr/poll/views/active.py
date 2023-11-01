from .blueprint import *


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