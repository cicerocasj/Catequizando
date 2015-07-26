# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app.catequista_model import Catequista
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions, login_required
from permission_app.model import ADMIN, COORDENADOR, validate_permission


@no_csrf
@login_required
def index(_logged_user):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    query = Catequista.query().order(Catequista.name)
    catequistas = query.fetch()
    context['catequistas'] = catequistas
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/index.html')