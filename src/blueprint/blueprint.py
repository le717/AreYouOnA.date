import time
from flask import Blueprint, request
from flask import render_template, url_for


bp = Blueprint("date", __name__, url_prefix="")


@bp.app_context_processor
def cache_buster():
    return {"cache_buster": time.time()}


@bp.route("/form", methods=["POST"])
def form() -> str:
    return url_for("date.no")


@bp.route("/")
def index() -> str:
    return render_template("permission.html")


@bp.route("/privacy")
def privacy() -> str:
    return render_template("privacy.html", page_title="Privacy")


@bp.route("/no")
def no() -> str:
    return render_template("no.html", page_title="No.")


@bp.route("/maybe")
def maybe() -> str:
    return render_template("maybe.html", page_title="Maybe...?")


@bp.route("/yes")
def yes() -> str:
    return render_template("yes.html", page_title="Yes!")
