from flask import render_template, g, jsonify

from ..core import db
from ..menu import menu, breadcrumb
from ..models import Instance
from . import bp


@bp.route('/')
@menu('index')
@breadcrumb('Home', '.index')
def index():
    return render_template('index.html')


@bp.route('/servers/server-list')
@menu('server_list')
@breadcrumb('List of servers', '.server_list')
def server_list():
    g.server_list = Instance.query.filter_by(enabled=True).all()
    return render_template('server_list.html')


@bp.route('/servers/<uuid>', methods=('DELETE',))
def remove_server(uuid):
    instance = Instance.query.filter_by(uuid=uuid).first()
    db.session.delete(instance)
    db.session.commit()
    return jsonify()


@bp.route('/statistics')
@menu('statistics')
@breadcrumb('Statistics', '.statistics')
def statistics():
    return render_template('statistics.html')
