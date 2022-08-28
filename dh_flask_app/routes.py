import sqlalchemy
from flask import Blueprint, request, jsonify, Response, redirect

from dh_flask_app.tools.urlParser import url_converter
from .extensions import db
from .models import Url
from .constants import *
from .tools.hasher import *

dhApp = Blueprint("main", __name__)


@dhApp.route("/<string:shortUrl>", methods=["GET"])
def short_url(shortUrl):
    """
    shortUrl has dynamic routing.
    :parameter shortUrl shortened url to redirect original url

    :rtype: redirects or json
    """
    try:
        if shortUrl in ["getAll", "addUrl", "isOnline"]:
            return jsonify({"status": "failed"}), INVALID_DATA
        url = Url.query.filter_by(shortUrl=shortUrl).first()
        url.counter += 1
        db.session.commit()
        return redirect(url_converter(url.url))
    except Exception as ex:
        return jsonify({"status": "failed", "Error": shortUrl+" doesnt exist"}), INVALID_DATA


@dhApp.route("/isOnline", methods=["GET"])
def isOnline():
    """
    checks if server is online

    :rtype: json
    """
    return jsonify({"status": "success"})


@dhApp.route("/addUrl/<urlOriginal>", methods=["GET"])
@dhApp.route("/addUrl", methods=["POST"])
def add_url(urlOriginal=None):
    """
    add_url has 2 routes:
    -/addUrl/{url}:
      This route takes url parameter from url
    -/addUrl
      This route take url from json (key:url)

    :parameter urlOriginal if rest method is get, than urlOriginal will be used. Otherwise url will be fetched from json

    :rtype: json or shortened url string
    """
    if request.method == "GET":
        url = urlOriginal
    if request.method == "POST":
        try:
            data = request.get_json()
            url = data["url"]
        except Exception as ex:
            return Response("Invalid Data:" + str(ex), INVALID_DATA, mimetype="application/json")
    urlHashed = ""
    while len(urlHashed) < 13:
        try:
            urlHashed = urlhasher(url, oldHash=urlHashed)
            urlObj = Url(url=url, shortUrl=urlHashed, counter=0)
            db.session.add(urlObj)
            db.session.commit()
            return request.host_url + urlHashed
        except sqlalchemy.exc.IntegrityError:
            db.session.rollback()
    return jsonify({"status": "failed"}), INVALID_DATA


@dhApp.route("/getAll", methods=["GET"])
def get_all_url():
    """
    Returns list of url with:
    -string: url
      original url
    -string: shortUrl
      shortened url
    -int: counter
       visit count of shortened url

    :rtype: json
    """
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
        return jsonify({"status": "failed", "Error": str(ex)}), INVALID_DATA
