# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app.catequista_model import Catequista
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import ADMIN, COORDENADOR


@no_csrf
@permissions(ADMIN, COORDENADOR)
def index():
    context = {}
    query = Catequista.query().order(Catequista.name)
    catequistas = query.fetch()
    context['catequistas'] = catequistas
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/index.html')