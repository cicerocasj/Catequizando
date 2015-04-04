# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app.catequista_model import Catequista
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index():
    context = {}
    query = Catequista.query().order(Catequista.key)
    catequistas = query.fetch()
    context['catequistas'] = catequistas
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/index.html')