# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from encontro_app.encontro_model import Encontro
from config.template_middleware import TemplateResponse


@no_csrf
def index():
    context = {}
    query = Encontro.query_by_creation_desc()
    meeting = query.fetch()
    context['meeting'] = meeting
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/index.html')