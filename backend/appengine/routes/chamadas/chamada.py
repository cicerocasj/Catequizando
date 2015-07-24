# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime
from time import sleep
from tekton import router
from catequizando_app.catequizando_model import Catequizando
from chamada_app import chamada_facade
from tekton.gae.middleware.redirect import RedirectResponse
from encontro_app.encontro_model import Encontro
from gaebusiness.business import CommandExecutionException
from routes import chamadas
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from turma_app.turma_model import Turma
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO, COMUM


@no_csrf
@permissions(ADMIN, COORDENADOR, CATEQUISTA)
def index(id=0):
    catequizandos = []
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        list_catequizandos = Catequizando.query(Catequizando.turma==Turma.get_by_id(key_id).key).fetch()
        for catequizando in list_catequizandos:
            catequizandos.append({'id': catequizando.key.id(), 'name': catequizando.name})
    else:
        list_catequizandos = []
    list_encontros = Encontro.query().fetch()
    encontros = []
    for encontro in list_encontros:
        encontros.append({'id': encontro.key.id(), 'name': encontro.title})

    turma = Turma.query()
    context = {
        'encontros': encontros,
        'turma': turma,
        'catequizandos': catequizandos,
        'nav_active': 'chamadas',
        'date': datetime.now().date().strftime('%d/%m/%Y'),
        'save': router.to_path(save),
        'turma_id': key_id
    }
    return TemplateResponse(context, template_path='/chamadas/chamada.html')


@permissions(ADMIN, COORDENADOR, CATEQUISTA)
@no_csrf
def save(**chamada_properties):
    if chamada_properties.get('encontro'):
        encontro = Encontro.get_by_id(int(chamada_properties.get('encontro')))
        chamada_properties['encontro'] = encontro
    if chamada_properties.get('turma'):
        turma = Turma.get_by_id(int(chamada_properties.get('turma')))
        chamada_properties['turma'] = turma
    if chamada_properties.get('catequizandos'):
        catequizandos = unicode(chamada_properties.get('catequizandos'))
        chamada_properties['catequizandos'] = catequizandos
    else:
        chamada_properties['catequizandos'] = unicode([])
    cmd = chamada_facade.save_chamada_cmd(**chamada_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'meeting': chamada_properties}
        return TemplateResponse(context, '/chamadas/chamada.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(chamadas))