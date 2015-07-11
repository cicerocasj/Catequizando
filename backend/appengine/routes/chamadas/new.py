# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from chamada_app import chamada_facade
from routes import chamadas
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'chamadas/chamada_form.html')


def save(**chamada_properties):
    cmd = chamada_facade.save_chamada_cmd(**chamada_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'chamada': chamada_properties}

        return TemplateResponse(context, 'chamadas/chamada_form.html')
    return RedirectResponse(router.to_path(chamadas))

