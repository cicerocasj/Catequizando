# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index(id):
    context = {}
    context["nav_active"] = 'catequista'
    context["id"] = id
    return TemplateResponse(context, template_path='/catequista/editar.html')