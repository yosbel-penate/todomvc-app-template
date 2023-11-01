from .blueprint import *
from ..model import get_question


@bp.route('/poll/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_question(id)
    db = get_db()
    db.execute('DELETE FROM question WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))