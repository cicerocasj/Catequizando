# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from turma_app.turma_model import Turma
from gaecookie.decorator import no_csrf


@no_csrf
def index():
    context = {}
    query = Turma.query_by_creation_desc()
    turmas = query.fetch()
    context['turmas'] = turmas
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/turmas/index.html')