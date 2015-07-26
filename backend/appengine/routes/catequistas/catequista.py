# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from permission_app.model import ALL_PERMISSIONS_LIST, validate_permission
from time import sleep
from catequista_app import catequista_facade
from catequista_app.catequista_model import Catequista
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_required
from routes import catequistas
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from user_app.user_model import User
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR


@no_csrf
@login_required
def index(_logged_user, id=0):
    access_invalid = validate_permission(ADMIN, _logged_user)
    if access_invalid:
        return access_invalid
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catequista"] = Catequista.get_by_id(key_id)
        url_form = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
        context["groups"] = context["catequista"].groups
    else:
        context["catequista"] = Catequista()
        url_form = router.to_path(save)
        context["groups"] = []
    list_permission = ALL_PERMISSIONS_LIST[:-1]
    context["choice_groups"] = list_permission
    context["url_form"] = url_form
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/catequista.html')


@permissions(ADMIN, COORDENADOR)
@no_csrf
def save(**catequistas_properties):
    if not isinstance(catequistas_properties.get('groups'), list):
        catequistas_properties['groups'] = [catequistas_properties.get('groups')]
    user_not_unique = False
    cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
    try:
        if catequistas_properties.get('username') and User.is_unique(catequistas_properties.get('username')):
            cmd()
        else:
            user_not_unique = True
    except CommandExecutionException:
        context = {
            'errors': cmd.errors,
            'catequista': catequistas_properties
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    if user_not_unique:
        cmd.errors['username'] = unicode(u'Usuário já existe.')
        context = {
            'errors': cmd.errors,
            'catequista': catequistas_properties,
            "groups": catequistas_properties.get('groups')
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@permissions(ADMIN, COORDENADOR, CATEQUISTA)
@no_csrf
def edit(**catequistas_properties):
    obj_id = catequistas_properties.pop("key_id", None)
    if not isinstance(catequistas_properties.get('groups'), list):
        catequistas_properties['groups'] = [catequistas_properties.get('groups')]
    cmd = catequista_facade.update_catequista_cmd(obj_id, **catequistas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': {},
                   'catequista': catequistas_properties}
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@permissions(ADMIN, COORDENADOR)
@no_csrf
def delete(obj_id=0):
    cmd = catequista_facade.delete_catequista_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))