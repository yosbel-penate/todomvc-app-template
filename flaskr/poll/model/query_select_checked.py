def query_select_checked(db):
    questions = db.execute(
        'SELECT q.id, body, is_checked, author_id, username'
        ' FROM question q JOIN user u ON q.author_id = u.id'
        ' WHERE is_checked = 1'
        ' ORDER BY created DESC'
    ).fetchall()
    return questions