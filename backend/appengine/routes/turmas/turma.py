# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["id"] = id
        context["type"] = u'Crisma 3'
        context["initial_hour"] = u'19:00'
        context["end_hour"] = u'20:00'
        context["local"] = u'paróquia São Sebastião'
        context["day"] = u'Quarta-feira'
        context["groups"] = [
            {'type': 'crisma 3', 'day': 'quarta', 'hours': '19:00 - 20:00', 'local': u'paróquia', 'catechized': 16}
        ]
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/turmas/turma.html')