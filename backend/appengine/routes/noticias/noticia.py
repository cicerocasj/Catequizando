# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from noticia_app.noticia_model import Noticia
from tekton import router
from gaecookie.decorator import no_csrf
from noticia_app import noticia_facade
from routes import noticias
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
        context["notice"] = Noticia.get_by_id(key_id)
        context["save_path"] = router.to_path(edit)
    else:
        context["notice"] = Noticia()
        context["save_path"] = router.to_path(save)
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/noticia.html')

@login_not_required
@no_csrf
def save(**noticia_properties):
    cmd = noticia_facade.save_noticia_cmd(**noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(noticias))


@login_not_required
@no_csrf
def edit(**noticia_properties):
    obj_id = noticia_properties.pop("key_id", None)
    cmd = noticia_facade.update_noticia_cmd(obj_id, **noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(noticias))