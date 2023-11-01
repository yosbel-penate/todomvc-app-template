from .blueprint import *
from ..model import query_delete_question_by_author_id

@bp.route('/poll/clearcomplete')
@login_required
def clear_complete():
    db = get_db()
    query_delete_question_by_author_id(db)
    return redirect(url_for('index'))
