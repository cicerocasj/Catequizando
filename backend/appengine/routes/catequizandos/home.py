# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequizando_app.catequizando_model import Catequizando
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index():
    context = {}
    query = Catequizando.query().order(Catequizando.name)
    catechizeds = query.fetch()
    context["catechizeds"] = catechizeds
    context["nav_active"] = 'catequizandos'
    return TemplateResponse(context, template_path='/catequizandos/index.html')