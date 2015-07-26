# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from noticia_app.noticia_model import Noticia
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions, login_required
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO, validate_permission


@login_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(CATEQUIZANDO, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    query = Noticia.query_by_creation_desc()
    noticias = query.fetch()
    context['notices'] = noticias
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/index.html')