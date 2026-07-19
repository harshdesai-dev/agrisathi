from flask import Blueprint, render_template, request
from db import query_db
from auth import login_required

bp = Blueprint("schemes", __name__, url_prefix="/schemes")


@bp.route("/")
@login_required
def index():
    search = request.args.get("q", "").strip()
    crop_id = request.args.get("crop_id", "").strip()

    sql = """
        SELECT s.id, s.scheme_name, s.benefit, s.action_link, s.crop_id,
               c.crop_name
        FROM schemes s
        LEFT JOIN crops c ON s.crop_id = c.id
        WHERE 1=1
    """
    args = []

    if search:
        sql += " AND (s.scheme_name LIKE %s OR s.benefit LIKE %s)"
        like = f"%{search}%"
        args.extend([like, like])

    if crop_id:
        sql += " AND s.crop_id = %s"
        args.append(crop_id)

    sql += " ORDER BY s.scheme_name"
    schemes = query_db(sql, tuple(args))

    # For the "filter by crop" dropdown
    crops = query_db("SELECT id, crop_name FROM crops ORDER BY crop_name")

    return render_template(
        "schemes/index.html",
        schemes=schemes,
        crops=crops,
        search=search,
        selected_crop_id=crop_id,
    )


@bp.route("/<int:scheme_id>")
@login_required
def detail(scheme_id):
    scheme = query_db(
        """SELECT s.*, c.crop_name FROM schemes s
           LEFT JOIN crops c ON s.crop_id = c.id
           WHERE s.id = %s""",
        (scheme_id,), one=True,
    )
    return render_template("schemes/detail.html", scheme=scheme)
