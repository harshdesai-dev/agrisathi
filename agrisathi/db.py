import mysql.connector
from flask import g, current_app


def get_db():
    """Get a MySQL connection, reused across the request via flask.g"""
    if "db" not in g:
        g.db = mysql.connector.connect(
            host=current_app.config["MYSQL_HOST"],
            user=current_app.config["MYSQL_USER"],
            password=current_app.config["MYSQL_PASSWORD"],
            database=current_app.config["MYSQL_DB"],
        )
    return g.db


def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    """Run a SELECT query. Returns list of dict rows, or single dict if one=True."""
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def execute_db(query, args=()):
    """Run an INSERT/UPDATE/DELETE. Returns the new row id (for INSERTs)."""
    conn = get_db()
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    new_id = cur.lastrowid
    cur.close()
    return new_id


def init_app(app):
    app.teardown_appcontext(close_db)
