def query_update_question(id, is_checked, db):
    db.execute(
            'UPDATE question SET is_checked = ?'
            ' WHERE id = ?',
            ( is_checked, id)
        )
    db.commit()