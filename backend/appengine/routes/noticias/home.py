# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from noticia_app.noticia_model import Noticia
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


@login_not_required
@no_csrf
def index():
    context = {}
    query = Noticia.query_by_creation_desc()
    noticias = query.fetch()
    context['notices'] = noticias
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/index.html')