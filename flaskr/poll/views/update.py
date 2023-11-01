from .blueprint import *
from ..model import query_update_question

@bp.route('/poll/update', methods=['POST'])
@login_required
def update():
    if request.method == 'POST':
        id = int(request.json['question_id'])
        is_checked = int(request.json['is_checked'])
        db = get_db()
        query_update_question(id, is_checked, db)
        return {'question_id': id, 'is_checked': is_checked, 'status': 'update'}

