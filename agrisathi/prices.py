from flask import Blueprint, render_template, request
from db import query_db
from auth import login_required

bp = Blueprint("prices", __name__, url_prefix="/prices")


@bp.route("/")
@login_required
def index():
    search = request.args.get("crop", "").strip()

    sql = "SELECT id, crop_name, market_price, msp_price, crop_status FROM crops WHERE 1=1"
    args = []
    if search:
        sql += " AND crop_name LIKE %s"
        args.append(f"%{search}%")

    sql += " ORDER BY crop_name"
    crops = query_db(sql, tuple(args))

    return render_template("prices/index.html", crops=crops, search=search)


@bp.route("/<int:crop_id>")
@login_required
def detail(crop_id):
    crop = query_db(
        "SELECT id, crop_name, market_price, msp_price, crop_status FROM crops WHERE id = %s",
        (crop_id,), one=True,
    )
    return render_template("prices/detail.html", crop=crop)
