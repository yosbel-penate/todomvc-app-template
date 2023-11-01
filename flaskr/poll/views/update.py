from .blueprint import *

@bp.route('/poll/update', methods=['POST'])
@login_required
def update():
    if request.method == 'POST':
        id = int(request.json['question_id'])
        is_checked = int(request.json['is_checked'])
        db = get_db()
        db.execute(
            'UPDATE question SET is_checked = ?'
            ' WHERE id = ?',
            ( is_checked, id)
        )
        db.commit()
        return {'question_id': id, 'is_checked': is_checked, 'status': 'update'}