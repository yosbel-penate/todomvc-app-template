from .blueprint import *
from ..model import query_select_non_checked_question

@bp.route('/poll/completed')
def completed():
    db = get_db()
    questions = query_select_non_checked_question(db)
    filter='completed'
    return render_template('poll/index.html', questions=questions, filter=filter )

