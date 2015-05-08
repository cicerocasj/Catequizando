# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from catequista_app.catequista_model import Catequista, TurmaCatequista
from catequizando_app import catequizando_facade
from catequizando_app.catequizando_model import Catequizando
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from turma_app.turma_commands import choice_catequizandos, catequizandos, selected_catequizandos, clean_turma, \
    choice_catequistas
from turma_app.turma_model import Turma
from tekton import router
from gaecookie.decorator import no_csrf
from turma_app import turma_facade
from routes import turmas
from tekton.gae.middleware.redirect import RedirectResponse
from gaegraph.model import ndb


@login_not_required
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
    context["choice_catequizandos"] = choice_catequizandos()
    context["choice_catequistas"] = choice_catequistas()
    if context["turma"].key:
        context["catequizandos"] = catequizandos(context["turma"].key)
        query = TurmaCatequista.query(TurmaCatequista.origin==context["turma"].key)
        catequistas = query.fetch()
        context["catequistas"] = [catequista.destination.get() for catequista in catequistas]
    else:
        context["catequizandos"] = []
        context["catequistas"] = []
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/turmas/turma.html')


@login_not_required
@no_csrf
def save(**turmas_properties):
    input_catequizandos = turmas_properties.pop("catequizandos", [])
    lista_catequizandos = input_catequizandos if isinstance(input_catequizandos, list) else [input_catequizandos]
    input_catequistas = turmas_properties.pop("catequistas", [])
    lista_catequistas = input_catequistas if isinstance(input_catequistas, list) else [input_catequistas]
    cmd = turma_facade.save_turma_cmd(**turmas_properties)
    try:
        turma = cmd()
    except CommandExecutionException:
        context = {
            'errors': cmd.errors,
            'turma': cmd.form,
            "choice_catequizandos": choice_catequizandos(),
            "catequizandos": selected_catequizandos(lista_catequizandos)
        }
        return TemplateResponse(context, template_path='turmas/turma.html')

    if lista_catequizandos:
        for key in lista_catequizandos:
            catequizando = Catequizando.get_by_id(int(key))
            catequizando.turma = turma.key
            catequizando.put()
    if lista_catequistas:
        for key in lista_catequistas:
            catequista = Catequista.get_by_id(int(key))
            turma_catequista = TurmaCatequista()
            turma_catequista.origin = turma.key
            turma_catequista.destination = catequista.key
            turma_catequista.put()
    sleep(0.5)
    return RedirectResponse(router.to_path(turmas))


@login_not_required
@no_csrf
def edit(**turmas_properties):
    data = turmas_properties.pop("catequizandos", None)
    if data:
        lista_catequizandos = data if isinstance(data, list) else [data]
    else:
        lista_catequizandos = None
    obj_id = turmas_properties.pop("key_id", None)
    cmd = turma_facade.update_turma_cmd(obj_id, **turmas_properties)
    try:
        turma = cmd()
    except CommandExecutionException:
        context = {
            'errors': cmd.errors,
            'turma': cmd.form,
            "choice_catequizandos": choice_catequizandos(),
            "catequizandos": selected_catequizandos(lista_catequizandos),
            'obj_id': obj_id
        }
        return TemplateResponse(context, template_path='turmas/turma.html')

    clean_turma(turma)
    if lista_catequizandos:
        for key in lista_catequizandos:
            catequizando = Catequizando.get_by_id(int(key))
            catequizando.turma = turma.key
            catequizando.put()
    sleep(0.5)
    return RedirectResponse(router.to_path(turmas))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = turma_facade.delete_turma_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, 'turmas/turma.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(turmas))