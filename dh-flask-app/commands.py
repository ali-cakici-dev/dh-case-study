import click
from flask.cli import with_appcontext
from .extensions import db
from .models import Url


@click.command(name="createDB")
@with_appcontext
def createDb():
    db.create_all()


@click.command(name="dropDB")
@with_appcontext
def dropDB():
    db.drop_all()

