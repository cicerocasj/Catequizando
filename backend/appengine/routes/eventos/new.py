# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from evento_app import evento_facade
from routes import eventos
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'eventos/evento_form.html')


def save(**evento_properties):
    cmd = evento_facade.save_evento_cmd(**evento_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'evento': evento_properties}

        return TemplateResponse(context, 'eventos/evento_form.html')
    return RedirectResponse(router.to_path(eventos))

