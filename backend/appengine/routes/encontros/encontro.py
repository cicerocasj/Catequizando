# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from encontro_app import encontro_facade
from encontro_app.encontro_model import Encontro
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from routes import encontros
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_required
from permission_app.model import COORDENADOR, validate_permission, CATEQUIZANDO


@login_required
@no_csrf
def index(_logged_user, id=0):
    access_denid = validate_permission(CATEQUIZANDO, _logged_user)
    if access_denid:
        return access_denid
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


@login_required
@no_csrf
def save(_logged_user, **encontro_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = encontro_facade.save_encontro_cmd(**encontro_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'meeting': encontro_properties}
        return TemplateResponse(context, '/encontros/encontro.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(encontros))


@login_required
@no_csrf
def edit(_logged_user, **encontro_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
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


@login_required
@no_csrf
def delete(_logged_user, obj_id=0):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = encontro_facade.delete_encontro_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, '/encontros/encontro.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(encontros))