# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required, login_required
from noticia_app.noticia_model import Noticia
from permission_app.model import validate_permission, CATEQUIZANDO, COORDENADOR
from tekton import router
from gaecookie.decorator import no_csrf
from noticia_app import noticia_facade
from routes import noticias
from tekton.gae.middleware.redirect import RedirectResponse


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
        context["notice"] = Noticia.get_by_id(key_id)
        context["save_path"] = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
    else:
        context["notice"] = Noticia()
        context["save_path"] = router.to_path(save)
    context["nav_active"] = 'noticias'
    return TemplateResponse(context, template_path='/noticias/noticia.html')

@login_required
@no_csrf
def save(_logged_user, **noticia_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = noticia_facade.save_noticia_cmd(**noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(noticias))


@login_required
@no_csrf
def edit(_logged_user, **noticia_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    obj_id = noticia_properties.pop("key_id", None)
    cmd = noticia_facade.update_noticia_cmd(obj_id, **noticia_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'noticia': noticia_properties}
        return TemplateResponse(context, 'noticias/noticia.html')
    return RedirectResponse(router.to_path(noticias))


@login_required
@no_csrf
def delete(_logged_user, obj_id=0):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = noticia_facade.delete_noticia_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, 'noticias/noticia.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(noticias))