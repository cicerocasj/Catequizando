# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from encontro_app.encontro_model import Encontro
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required, login_required
from permission_app.model import validate_permission, CATEQUISTA, CATEQUIZANDO


@login_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(CATEQUIZANDO, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    query = Encontro.query_by_creation_desc()
    meeting = query.fetch()
    context['meetings'] = meeting
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/index.html')