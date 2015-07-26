# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from time import sleep
from catequizando_app import catequizando_facade
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, login_required
from permission_app.model import validate_permission, COORDENADOR
from routes import catequizandos
from routes.catequizandos import download
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from turma_app.turma_model import Turma
from user_app.user_model import User


@login_required
@no_csrf
def index(_logged_user, _handler, **catequizando_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    if catequizando_properties.get("files"):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequizando_properties["avatar"] = avatar
        catequizando_properties.pop("files", None)
    cmd = catequizando_facade.save_catequizando_cmd(**catequizando_properties)
    user_not_unique = False
    try:
        if catequizando_properties.get('username') and User.is_unique(catequizando_properties.get('username')):
            cmd()
        else:
            user_not_unique = True
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catechized': catequizando_properties}
        return TemplateResponse(context, '/catequizandos/catequizando.html')
    if user_not_unique:
        cmd.errors['username'] = unicode(u'Usuário já existe.')
        context = {'errors': cmd.errors,
                   'catechized': catequizando_properties}
        return TemplateResponse(context, '/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))


@login_required
@no_csrf
def edit(_logged_user, _handler, **catequizandos_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
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


@login_required
@no_csrf
def delete(_logged_user, obj_id=0):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = catequizando_facade.delete_catequizando_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))