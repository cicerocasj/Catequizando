# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from turma_app.turma_model import Turma
from tekton import router
from gaecookie.decorator import no_csrf
from turma_app import turma_facade
from routes import turmas
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["turma"] = Turma.get_by_id(key_id)
        context["save_path"] = router.to_path(edit)
    else:
        context["save_path"] = router.to_path(save)
        context["turma"] = Turma()
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/turmas/turma.html')


def save(**turmas_properties):
    cmd = turma_facade.save_turma_cmd(**turmas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'turma': turmas_properties}
        return TemplateResponse(context, 'turmas/turma.html')
    return RedirectResponse(router.to_path(turmas))


def edit(**turmas_properties):
    obj_id = turmas_properties.pop("key_id", None)
    cmd = turma_facade.update_turma_cmd(obj_id, **turmas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'turma': turmas_properties}
        return TemplateResponse(context, 'turmas/turma.html')
    return RedirectResponse(router.to_path(turmas))