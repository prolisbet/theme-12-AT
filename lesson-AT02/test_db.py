import pytest
from main_db import init_db, add_user, get_user


@pytest.fixture
def db_conn():
    conn = init_db()
    yield conn
    conn.close()


def test_add_or_get_user(db_conn):
    add_user(db_conn, 'Alice', 25)
    user = get_user(db_conn, 'Alice')
    assert user == (1, 'Alice', 25)
