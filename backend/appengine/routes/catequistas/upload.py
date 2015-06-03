# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from catequista_app import catequista_facade
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import catequistas
from routes.catequistas import download
from tekton import router
from tekton.router import to_path
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index(_handler, **catequistas_properties):
    if catequistas_properties.get('files'):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequistas_properties['avatar'] = avatar
        catequistas_properties.pop("files", None)
    cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {
            'errors': cmd.errors
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@login_not_required
@no_csrf
def edit(_handler, **catequistas_properties):
    if catequistas_properties.get('files'):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequistas_properties['avatar'] = avatar
        catequistas_properties.pop("files", None)
    obj_id = catequistas_properties.pop("key_id", None)
    cmd = catequista_facade.update_catequista_cmd(obj_id, **catequistas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catequista': catequistas_properties}
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = catequista_facade.delete_catequista_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))