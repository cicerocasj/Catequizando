# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from evento_app.evento_model import Evento
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    context = {}
    query = Evento.query_by_creation_desc()
    eventos = query.fetch()
    context['eventos'] = eventos
    context["nav_active"] = 'eventos'
    return TemplateResponse(context, template_path='/eventos/index.html')