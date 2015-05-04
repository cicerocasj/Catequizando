# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from time import sleep
from catequizando_app import catequizando_facade
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import catequizandos
from routes.catequizandos import download
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from turma_app.turma_model import Turma


@login_not_required
@no_csrf
def index(_handler, **catequizando_properties):
    if catequizando_properties.get("files"):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequizando_properties["avatar"] = avatar
        catequizando_properties.pop("files", None)
    cmd = catequizando_facade.save_catequizando_cmd(**catequizando_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catechized': catequizando_properties}
        return TemplateResponse(context, '/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))


@login_not_required
@no_csrf
def edit(_handler, **catequizandos_properties):
    if catequizandos_properties.get('files'):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequizandos_properties['avatar'] = avatar
        catequizandos_properties.pop("files", None)
    obj_id = catequizandos_properties.pop("key_id", None)
    cmd = catequizando_facade.update_catequizando_cmd(obj_id, **catequizandos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catequista': catequizandos_properties}
        return TemplateResponse(context, template_path='/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = catequizando_facade.delete_catequizando_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))