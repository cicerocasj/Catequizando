# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from noticia_app.noticia_model import Noticia
from tekton import router
from gaecookie.decorator import no_csrf
from noticia_app import noticia_facade
from routes import noticias
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["notice"] = Noticia.get_by_id(key_id)
    context["nav_active"] = 'noticias'
    context["save_path"] = router.to_path(save)
    return TemplateResponse(context, template_path='/noticias/noticia.html')


def save(**noticia_properties):
    cmd = noticia_facade.save_noticia_cmd(**noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(noticias))