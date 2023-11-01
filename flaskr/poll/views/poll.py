from .blueprint import *
from ..model import query_get_all_questions, query_get_questions_by_user_id

@bp.route('/')
def poll():
    db = get_db()
    questions = ...
    if g.user:
        questions = query_get_questions_by_user_id(db)
    else:
        questions = query_get_all_questions(db)
    filter='all'
    return render_template('poll/index.html', questions=questions, filter=filter)

