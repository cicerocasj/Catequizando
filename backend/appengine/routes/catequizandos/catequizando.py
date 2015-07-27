# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from permission_app.model import ALL_PERMISSIONS_LIST, validate_permission, set_permission
from routes.catequizandos import upload
from time import sleep
from catequizando_app import catequizando_facade
from catequizando_app.catequizando_model import Catequizando
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required, login_required
from routes import catequizandos
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from user_app.user_model import User
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO, COMUM


@no_csrf
@login_required
def index(_logged_user, id=0):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catequizando"] = Catequizando.get_by_id(key_id)
        url_form = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
        context["groups"] = context["catequizando"].groups
    else:
        context["catequizando"] = Catequizando()
        url_form = router.to_path(save)
        context["groups"] = []
    list_permission = ALL_PERMISSIONS_LIST[:-1]
    context["choice_groups"] = list_permission
    context["sugestao"] = "catequizando{}".format(Catequizando.query().count()+1)
    context["url_form"] = url_form
    context["nav_active"] = 'catequizandos'
    return TemplateResponse(context, template_path='/catequizandos/catequizando.html')


@login_required
def save(_logged_user, **catequizandos_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    catequizandos_properties['groups'] = [CATEQUIZANDO, COMUM]
    erros = {}
    cmd = catequizando_facade.save_catequizando_cmd(**catequizandos_properties)
    try:
        username_is_unique = catequizandos_properties.get('username') and User.is_unique(catequizandos_properties.get('username'))
        email_is_unique = User.is_unique_email(catequizandos_properties.get('email'))
        if not username_is_unique:
            erros['username'] = unicode(u'Usuário já existe.')
        if not email_is_unique:
            erros['email'] = unicode(u'Email já utilizado.')
        if username_is_unique and email_is_unique:
            cmd()
    except CommandExecutionException:
        context = {
            'errors': cmd.errors,
            'catequizando': catequizandos_properties
        }
        return TemplateResponse(context, template_path='/catequizandos/catequizando.html')
    if erros:
        context = {
            'errors': erros,
            'catequizando': catequizandos_properties,
            "groups": catequizandos_properties.get('groups')
        }
        return TemplateResponse(context, template_path='/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))


@login_required
def edit(_logged_user, **catequizandos_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    obj_id = catequizandos_properties.pop("key_id", None)
    catequizandos_properties['groups'] = [CATEQUIZANDO, COMUM]
    cmd = catequizando_facade.update_catequizando_cmd(obj_id, **catequizandos_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': {},
                   'catequizando': catequizandos_properties}
        return TemplateResponse(context, template_path='/catequizandos/catequizando.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequizandos))


@login_required
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