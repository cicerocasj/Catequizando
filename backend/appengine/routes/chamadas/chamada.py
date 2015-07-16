# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime
from catequista_app.catequista_model import TurmaCatequista
from catequizando_app.catequizando_model import Catequizando
from chamada_app.chamada_commands import choice_turmas
from encontro_app.encontro_model import Encontro
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
        'date': datetime.now().date().strftime('%d/%m/%Y')
    }
    return TemplateResponse(context, template_path='/chamadas/chamada.html')