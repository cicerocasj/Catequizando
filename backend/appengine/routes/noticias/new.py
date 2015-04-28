# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from tekton import router
from gaecookie.decorator import no_csrf
from noticia_app import noticia_facade
from routes import noticias
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'noticias/noticia_form.html')


@login_not_required
@no_csrf
def save(**noticia_properties):
    cmd = noticia_facade.save_noticia_cmd(**noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}

        return TemplateResponse(context, 'noticias/noticia_form.html')
    return RedirectResponse(router.to_path(noticias))

