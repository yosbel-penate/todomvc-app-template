from .blueprint import *
from ..model import query_select_checked


@bp.route('/poll/active')
def active():
    db = get_db()
    questions = query_select_checked(db)
    filter = 'active'
    return render_template('poll/index.html', questions=questions, filter=filter)
