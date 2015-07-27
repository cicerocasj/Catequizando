# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from evento_app.evento_model import Evento
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from permission_app.model import validate_permission, CATEQUIZANDO


@login_not_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(CATEQUIZANDO, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    query = Evento.query().order(Evento.title)
    eventos = query.fetch()
    context['eventos'] = eventos
    context["nav_active"] = 'eventos'
    return TemplateResponse(context, template_path='/eventos/index.html')