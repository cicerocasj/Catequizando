# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse


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
    context["nav_active"] = 'chamadas'




    if key_id:
        context["id"] = id
        context["groups"] = u'Cícero Alves dos Santos Junior'
        context["date"] = u'1111-11-13'
        context["name"] = u'Crisma 2  - Cícero Alves'
    context["catechized"] = [
        u"Ailton Gamarra", u'Debora de Souza', u'Maicon Dias', u'Edson Silva', u'Michel Bastos',
        u'Luiz Fabiano', u'Reinaldo Velazques', u'Bruno Dias', u'Margarida Mota', u'Francisco Paiva',
        u'Tatiana Almeida', u'Celso Alves'
    ]

    return TemplateResponse(context, template_path='/chamadas/chamada.html')