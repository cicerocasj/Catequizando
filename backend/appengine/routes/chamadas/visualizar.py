# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequizando_app.catequizando_model import Catequizando
from chamada_app.chamada_model import Chamada
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from turma_app.turma_model import Turma


@login_not_required
@no_csrf
def index(_logged_user, id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        turma = Turma.get_by_id(key_id)
        chamadas = Chamada.query(Chamada.turma==turma.key).order(Chamada.data).fetch()
        catequizandos = Catequizando.query(Catequizando.turma==turma.key).fetch()
        context["id"] = id
        context["turma"] = turma
        context["_logged_user"] = _logged_user
        context["groups"] = u'Cícero Alves dos Santos Junior'
        list_chamadas = []
        list_encontros = []
        first_loop = True

        for obj_cat in catequizandos:
            list_foi = []
            for chamada in chamadas:
                list_foi.append(unicode(obj_cat.key.id()) in chamada.catequizandos)
                if first_loop:
                    list_encontros.append(chamada.data.strftime('%d/%m'))
            first_loop = False
            list_chamadas.append({
                'name': obj_cat.name,
                'foi': list_foi,
            })
        context["chamadas"] = list_chamadas
        context["encontros"] = list_encontros
    context["nav_active"] = 'turmas'
    return TemplateResponse(context, template_path='/chamadas/visualizar.html')