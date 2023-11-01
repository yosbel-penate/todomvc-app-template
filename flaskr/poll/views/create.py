from .blueprint import *

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
            db.execute(
                'INSERT INTO question ( body, is_checked, author_id)'
                ' VALUES (?, ?, ?)',
                ( body, is_checked, g.user['id'])
            )
            db.commit()
            return redirect(url_for('index'))

    return render_template('poll/index.html')