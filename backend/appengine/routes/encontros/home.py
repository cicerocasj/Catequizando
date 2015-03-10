# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index():
    context = {}
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/index.html')