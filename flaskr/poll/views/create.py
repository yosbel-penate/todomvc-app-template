from .blueprint import *
from ..model import query_insert_question

@bp.route('/poll/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        body = request.form['body']
        error = None

        if not body:
            error = 'Question body is required.'

        if error is not None:
            flash(error)
        else:
            is_checked = 0
            db = get_db()
            query_insert_question(body, is_checked, db)
            return redirect(url_for('index'))

    return render_template('poll/index.html')

