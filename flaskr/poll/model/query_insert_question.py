from flaskr.poll.views.blueprint import g


def query_insert_question(body, is_checked, db):
    db.execute(
                'INSERT INTO question ( body, is_checked, author_id)'
                ' VALUES (?, ?, ?)',
                ( body, is_checked, g.user['id'])
            )
    db.commit()