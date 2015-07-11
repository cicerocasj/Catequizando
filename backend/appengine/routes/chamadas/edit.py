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
def index(chamada_id):
    chamada = chamada_facade.get_chamada_cmd(chamada_id)()
    chamada_form = chamada_facade.chamada_form()
    context = {'save_path': router.to_path(save, chamada_id), 'chamada': chamada_form.fill_with_model(chamada)}
    return TemplateResponse(context, 'chamadas/chamada_form.html')


def save(chamada_id, **chamada_properties):
    cmd = chamada_facade.update_chamada_cmd(chamada_id, **chamada_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'chamada': chamada_properties}

        return TemplateResponse(context, 'chamadas/chamada_form.html')
    return RedirectResponse(router.to_path(chamadas))

