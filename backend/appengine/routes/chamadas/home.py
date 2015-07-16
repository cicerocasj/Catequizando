# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from chamada_app.chamada_commands import choice_turmas
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from permission_app.model import COORDENADOR, ADMIN


@login_not_required
@no_csrf
def index(_logged_user):
    context = {}
    all = True if COORDENADOR in _logged_user.groups or ADMIN in _logged_user.groups else False
    choice = choice_turmas(_logged_user, all)
    context['turmas'] = choice
    context["nav_active"] = 'chamadas'
    return TemplateResponse(context, template_path='/chamadas/index.html')