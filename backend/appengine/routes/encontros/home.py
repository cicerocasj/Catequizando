# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from encontro_app.encontro_model import Encontro
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    context = {}
    query = Encontro.query_by_creation_desc()
    meeting = query.fetch()
    context['meetings'] = meeting
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/index.html')