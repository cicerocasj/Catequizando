# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from encontro_app import encontro_facade
from encontro_app.encontro_model import Encontro
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from routes import encontros
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
        context["meeting"] = Encontro.get_by_id(key_id)
        context["save_path"] = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
    else:
        context["meeting"] = Encontro()
        context["save_path"] = router.to_path(save)
    context["nav_active"] = 'encontros'
    return TemplateResponse(context, template_path='/encontros/encontro.html')


@login_not_required
@no_csrf
def save(**encontro_properties):
    cmd = encontro_facade.save_encontro_cmd(**encontro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'meeting': encontro_properties}
        return TemplateResponse(context, '/encontros/encontro.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(encontros))


@login_not_required
@no_csrf
def edit(**encontro_properties):
    obj_id = encontro_properties.pop("key_id", None)
    cmd = encontro_facade.update_encontro_cmd(obj_id, **encontro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'meeting': encontro_properties}
        return TemplateResponse(context, '/encontros/encontro.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(encontros))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = encontro_facade.delete_encontro_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, '/encontros/encontro.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(encontros))