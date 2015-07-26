# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequizando_app.catequizando_model import Catequizando
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions, login_required
from config.template_middleware import TemplateResponse
from permission_app.model import validate_permission, COORDENADOR


@login_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    query = Catequizando.query().order(Catequizando.name)
    catechizeds = query.fetch()
    context["catechizeds"] = catechizeds
    context["nav_active"] = 'catequizandos'
    return TemplateResponse(context, template_path='/catequizandos/index.html')