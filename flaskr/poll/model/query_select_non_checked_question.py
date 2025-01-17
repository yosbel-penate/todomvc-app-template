def query_select_non_checked_question(db):
    questions = db.execute(
        'SELECT q.id, body, is_checked, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' WHERE is_checked = 0'
        ' ORDER BY created DESC'
    ).fetchall()
    return questions