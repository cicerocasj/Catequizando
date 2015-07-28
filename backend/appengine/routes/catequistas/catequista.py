# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from permission_app.model import ALL_PERMISSIONS_LIST, validate_permission, set_permission
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
    access_denid = validate_permission(CATEQUISTA, _logged_user)
    if access_denid:
        return access_denid
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catequista"] = Catequista.get_by_id(key_id)
        url_form = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
        context["groups"] = context["catequista"].groups[0] if context["catequista"].groups else []
    else:
        context["catequista"] = Catequista()
        url_form = router.to_path(save)
        context["groups"] = []
    list_permission = ALL_PERMISSIONS_LIST[2:-1]
    context["choice_groups"] = list_permission
    context["sugestao"] = "catequista{}".format(Catequista.query().count()+1)
    context["url_form"] = url_form
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/catequista.html')


@login_required
def save(_logged_user, **catequistas_properties):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    catequistas_properties['groups'] = set_permission(catequistas_properties.get('groups'))
    erros = {}
    list_permission = ALL_PERMISSIONS_LIST[2:-1]
    cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
    try:
        username_is_unique = catequistas_properties.get('username') and User.is_unique(catequistas_properties.get('username'))
        email_is_unique = catequistas_properties.get('email') and User.is_unique_email(catequistas_properties.get('email'))
        if not username_is_unique:
            erros['username'] = unicode(u'Usuário já existe.')
        if not email_is_unique:
            erros['email'] = unicode(u'Email já utilizado.')
        if username_is_unique and email_is_unique:
            cmd()
    except CommandExecutionException:

        context = {
            'errors': cmd.errors,
            'choice_groups': list_permission,
            'catequista': catequistas_properties
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    if erros:
        context = {
            'errors': erros,
            'choice_groups': list_permission,
            'catequista': catequistas_properties,
            "groups": catequistas_properties.get('groups')
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@login_required
def edit(_logged_user, **catequistas_properties):
    access_denid = validate_permission(CATEQUISTA, _logged_user)
    erros = {}
    if access_denid:
        return access_denid
    obj_id = catequistas_properties.pop("key_id", None)
    catequistas_properties['groups'] = set_permission(catequistas_properties.get('groups'))
    user_not_unique = False
    list_permission = ALL_PERMISSIONS_LIST[2:-1]
    cmd = catequista_facade.update_catequista_cmd(obj_id, **catequistas_properties)
    try:
        cat = Catequista.get_by_id(int(obj_id))
        username_is_unique = catequistas_properties.get('username') and User.alter_user(cat.username, catequistas_properties.get('username'))
        email_is_unique = catequistas_properties.get('email') and User.alter_user_email(cat.email, catequistas_properties.get('email'))
        if not username_is_unique:
            erros['username'] = unicode(u'Usuário já existe.')
        if not email_is_unique:
            erros['email'] = unicode(u'Email já utilizado.')
        if username_is_unique and email_is_unique:
            cmd()
    except CommandExecutionException:
        context = {'errors': {},
                   'choice_groups': list_permission,
                   'catequista': catequistas_properties}
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    if user_not_unique:
        cmd.errors['username'] = unicode(u'Usuário já existe.')
        context = {
            'errors': cmd.errors,
            'choice_groups': list_permission,
            'catequista': catequistas_properties,
            "groups": catequistas_properties.get('groups')
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse('/sucesso')


@login_required
def delete(_logged_user, obj_id=0):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    cmd = catequista_facade.delete_catequista_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))