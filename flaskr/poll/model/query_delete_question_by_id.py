def query_delete_question_by_id(id, db):
    db.execute('DELETE FROM question WHERE id = ?', (id,))
    db.commit()