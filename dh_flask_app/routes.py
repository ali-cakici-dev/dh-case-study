import sqlalchemy
from flask import Blueprint, request, jsonify, Response, redirect

from dh_flask_app.tools.urlParser import url_converter
from .extensions import db
from .models import Url
from .constants import *
from .tools.hasher import *

dhApp = Blueprint("main", __name__)


@dhApp.route("/isOnline", methods=["GET"])
def root():
    return jsonify({"status": "success"})


@dhApp.route("/addURl", methods=["POST"])
def add_url():
    try:
        data = request.get_json()
    except Exception as ex:
        return Response("Invalid Data:" + str(ex), INVALID_DATA, mimetype="application/json")
    urlHashed = ""
    while len(urlHashed) < 13:
        try:
            urlHashed = urlhasher(data["url"], oldHash=urlHashed)
            url = Url(url=data["url"], shortUrl=urlHashed, counter=0)
            db.session.add(url)
            db.session.commit()
            return jsonify({"status": "success", "shortUrl": urlHashed})
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
    return jsonify({"status": "failed"}), INVALID_DATA


@dhApp.route("/<shortUrl>", methods=["GET"])
def short_url(shortUrl):
    try:
        url = Url.query.filter_by(shortUrl=shortUrl).first()
        url.counter += 1
        db.session.commit()
        return redirect(url_converter(url.url))
    except Exception as ex:
        return jsonify({"status": "failed", "Error": ex}), INVALID_DATA


@dhApp.route("/getAll", methods=["GET"])
def get_all_url():
    try:
        result = []
        urls = Url.query.all()
        for url in urls:
            result.append({
                "url": url.url,
                "shortUrl": url.shortUrl,
                "counter": url.counter
            })
        return jsonify({"status": "success", "urls": result}), OK
    except Exception as ex:
        return jsonify({"status": "failed", "Error": ex}), INVALID_DATA
