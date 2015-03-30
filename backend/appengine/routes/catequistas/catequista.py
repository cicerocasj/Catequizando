# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app import catequista_facade
from catequista_app.catequista_model import Catequista
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from routes import catequistas
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catequista"] = Catequista.get_by_id(key_id)
    context["nav_active"] = 'catequistas'
    context["save_path"] = router.to_path(save)
    return TemplateResponse(context, template_path='/catequistas/catequista.html')


def save(**catequista_properties):
    cmd = catequista_facade.save_catequista_cmd(**catequista_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catequista': catequista_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(catequistas))