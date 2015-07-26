# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from chamada_app.chamada_commands import choice_turmas
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required, login_required
from permission_app.model import validate_permission, COORDENADOR, ADMIN, CATEQUISTA
from turma_app.turma_commands import count_catequizandos
from turma_app.turma_model import Turma
from gaecookie.decorator import no_csrf


@login_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(CATEQUISTA, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    all = True if COORDENADOR in _logged_user.groups or ADMIN in _logged_user.groups else False
    choice = choice_turmas(_logged_user, all)
    context['turmas'] = choice

    context['count_catequizandos'] = count_catequizandos
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/turmas/index.html')