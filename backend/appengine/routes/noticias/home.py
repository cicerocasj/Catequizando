# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from noticia_app.noticia_model import Noticia
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse


@no_csrf
def index():
    context = {}
    query = Noticia.query_by_creation_desc()
    noticias = query.fetch()
    context['notices'] = noticias
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/index.html')