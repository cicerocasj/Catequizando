# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from encontro_app import encontro_facade
from encontro_app.encontro_model import Encontro
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from routes import encontros
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["meeting"] = Encontro.get_by_id(key_id)
    context["save_path"] = router.to_path(save)
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/encontro.html')


def save(**encontro_properties):
    cmd = encontro_facade.save_encontro_cmd(**encontro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'meeting': encontro_properties}
        return TemplateResponse(context, '/encontros/encontro.html')
    return RedirectResponse(router.to_path(encontros))