from flaskr.poll.views.blueprint import g


def query_get_questions_by_user_id(db):
    questions = db.execute(
            'SELECT q.id, body, is_checked, author_id, username'
            ' FROM question q JOIN user u ON q.author_id = u.id'
            ' WHERE u.id = ?'
            ' ORDER BY created DESC',
            ( g.user['id'],)
        ).fetchall()
    return questions