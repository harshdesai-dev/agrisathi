from flask import Blueprint, render_template, session
from db import query_db
from auth import login_required

bp = Blueprint("dashboard", __name__)


@bp.route("/")
@login_required
def index():
    latest_schemes = query_db(
        """SELECT s.id, s.scheme_name, c.crop_name FROM schemes s
           LEFT JOIN crops c ON s.crop_id = c.id
           ORDER BY s.id DESC LIMIT 4"""
    )
    latest_prices = query_db(
        "SELECT id, crop_name, market_price, msp_price FROM crops ORDER BY id DESC LIMIT 5"
    )
    return render_template(
        "dashboard.html",
        latest_schemes=latest_schemes,
        latest_prices=latest_prices,
        user_name=session.get("user_name"),
    )
