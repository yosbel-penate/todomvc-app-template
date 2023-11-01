from .blueprint import *
from ..model import get_question
from ..model import query_delete_question_by_id


@bp.route('/poll/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_question(id)
    db = get_db()
    query_delete_question_by_id(id, db)
    return redirect(url_for('index'))

