import pytest
from flaskr.db import get_db

def test_index(client, auth):
    response = client.get('/')
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get('/')
    assert b'Log Out' in response.data
    assert b'test\nbody' in response.data

@pytest.mark.parametrize('path', (
    '/poll/create',
    '/poll/update',
    '/poll/1/delete',
))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "/auth/login"

def test_author_required(app, client, auth):
    # change the post author to another user
    with app.app_context():
        db = get_db()
        db.execute('UPDATE question SET author_id = 2 WHERE id = 1')
        db.commit()

    auth.login()
    # current user can't modify other user's post
    assert client.post('/poll/1/delete').status_code == 403
    # current user doesn't see edit link
    assert b'href="/poll/update"' not in client.get('/').data

def test_create(client, auth, app):
    auth.login()
    assert client.get('/poll/create').status_code == 200
    client.post('/poll/create', data={'body': 'This is a Test'})

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM question').fetchone()[0]
        assert count == 2

def test_delete(client, auth, app):
    auth.login()
    response = client.post('/poll/1/delete')
    assert response.headers["Location"] == "/"

    with app.app_context():
        db = get_db()
        question = db.execute('SELECT * FROM question WHERE id = 1').fetchone()
        assert question is None