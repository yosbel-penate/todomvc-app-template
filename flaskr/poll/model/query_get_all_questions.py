def query_get_all_questions(db):
    questions = db.execute(
            'SELECT q.id, body, is_checked, author_id, username'
            ' FROM question q JOIN user u ON q.author_id = u.id'
            ' ORDER BY created DESC'
        ).fetchall()
    return questions