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
        context["title"] = u'Papa fala com os jovens'
        context["description"] = u"Formação para catequistas de toda a paróquia são sebastião. Quem não participar não poderá pegar uma turma"
        context["guests"] = ["Cícero Alves", "Erich Rodrigues", "Dona Rita", "Dona Cida", "Gilson", "João Camargo"]
        context["confirmed"] = ["João Camargo"]
        context["initial_date"] = "11/03/2015"
        context["initial_hour"] = "19:00"
        context["end_date"] = "12/03/2015"
        context["end_hour"] = "21:00"
    context["nav_active"] = 'eventos'
    return TemplateResponse(context, template_path='/eventos/evento.html')