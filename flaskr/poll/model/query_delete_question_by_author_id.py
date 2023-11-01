from ..views.blueprint import g, get_db


def query_delete_question_by_author_id(db):
    db.execute('DELETE FROM question WHERE author_id = ?', (g.user['id'],))
    db.commit()