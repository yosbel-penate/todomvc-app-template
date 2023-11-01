from .blueprint import *

@bp.route('/poll/clearcomplete')
@login_required
def clear_complete():
    db = get_db()
    db.execute('DELETE FROM question WHERE author_id = ?', (g.user['id'],))
    db.commit()
    return redirect(url_for('index'))