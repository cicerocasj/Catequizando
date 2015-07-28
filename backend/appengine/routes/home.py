# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from encontro_app.encontro_model import Encontro
from evento_app.evento_model import Evento
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions, login_required
from noticia_app.noticia_model import Noticia
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO, validate_permission


def time_ago(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "agora"
        if second_diff < 60:
            return str(second_diff) + " segundo atrás"
        if second_diff < 120:
            return "um minuto atrás"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutos atrás"
        if second_diff < 7200:
            return "uma hora atrás"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Ontem"
    if day_diff < 7:
        return str(day_diff) + " dias atrás"
    if day_diff < 31:
        return str(day_diff / 7) + " semanas atrás"
    if day_diff < 365:
        return str(day_diff / 30) + " meses atrás"
    return str(day_diff / 365) + " anos atrás"

# def time_ago(data):
#     return 'aaaaaa'

@no_csrf
@login_required
def index(_logged_user):
    context = {}
    messages = []
    list_eventos = Evento.query().fetch()
    list_noticias = Noticia.query().fetch()
    for noticia in list_noticias:
        messages.append({
        u'type': u'notice',
        u'id': noticia.key.id(),
        u'date': time_ago(noticia.creation),
        u'title': noticia.title,
        u'content': noticia.content
    })
    for evento in list_eventos:
        messages.append({
        u'type': u'event',
        u'id': evento.key.id(),
        u'date': time_ago(evento.creation),
        u'title': evento.title,
        u'content': evento.description
    })
    newlist = sorted(messages, key=lambda k: k['date'])
    context["messages"] = newlist
    context["nav_active"] = 'início'
    return TemplateResponse(context)

