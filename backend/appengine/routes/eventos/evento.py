# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from evento_app import evento_facade
from evento_app.evento_model import Evento
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_not_required
from routes import eventos
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
        context["evento"] = Evento.get_by_id(key_id)
        context["save_path"] = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
    else:
        context["evento"] = Evento()
        context["save_path"] = router.to_path(save)
    context["nav_active"] = 'eventos'
    return TemplateResponse(context, template_path='/eventos/evento.html')


@login_not_required
@no_csrf
def save(**evento_properties):
    cmd = evento_facade.save_evento_cmd(**evento_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'evento': evento_properties}
        return TemplateResponse(context, '/eventos/evento.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(eventos))


@login_not_required
@no_csrf
def edit(**evento_properties):
    obj_id = evento_properties.pop("key_id", None)
    cmd = evento_facade.update_evento_cmd(obj_id, **evento_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'evento': evento_properties}
        return TemplateResponse(context, '/eventos/evento.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(eventos))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = evento_facade.delete_evento_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, '/eventos/evento.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(eventos))