from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import query_db, execute_db
import functools

bp = Blueprint("auth", __name__, url_prefix="/auth")


def login_required(view):
    """Decorator: redirect to login if no user in session."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get("user_id") is None:
            flash("Please log in first.", "error")
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        error = None
        if not username or not password:
            error = "Username and password are required."

        if error is None:
            existing = query_db("SELECT id FROM users WHERE username = %s", (username,), one=True)
            if existing:
                error = f"Username '{username}' is already taken."

        if error is None:
            execute_db(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, generate_password_hash(password)),
            )
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for("auth.login"))

        flash(error, "error")

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        error = None
        user = query_db("SELECT * FROM users WHERE username = %s", (username,), one=True)

        if user is None:
            error = "Incorrect username or password."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect username or password."

        if error is None:
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["username"]
            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for("dashboard.index"))

        flash(error, "error")

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))
