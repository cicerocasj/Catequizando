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
        context["id"] = id
        context["groups"] = u'Cícero Alves dos Santos Junior'
        context["catechized"] = [
            {'name': u"Ailton Gamarra", 'presents': [False, True, True, False, True]},
            {'name': u"Debora de Souza", 'presents': [False, True, True, True, True]},
            {'name': u"Maicon Dias", 'presents': [False, False, True, False, True]},
            {'name': u"Edson Silva", 'presents': [False, True, True, True, True]},
            {'name': u"Michel Bastos", 'presents': [False, False, False, False, True]},
            {'name': u"Luiz Fabiano", 'presents': [False, True, True, True, True]},
            {'name': u"Reinaldo Velazques", 'presents': [False, True, True, False, True]},
            {'name': u"Bruno Dias", 'presents': [False, True, True, False, True]},
            {'name': u"Margarida Mota", 'presents': [False, True, False, False, True]},
            {'name': u"Francisco Paiva", 'presents': [True, True, True, False, True]},
            {'name': u"Tatiana Almeida", 'presents': [False, True, True, False, True]},
            {'name': u"Celso Alves", 'presents': [False, True, True, False, True]}
        ]
        # context["catechized"] = [
        #     u"Ailton Gamarra", u'Debora de Souza', u'Maicon Dias', u'Edson Silva', u'Michel Bastos',
        #     u'Luiz Fabiano', u'Reinaldo Velazques', u'Bruno Dias', u'Margarida Mota', u'Francisco Paiva',
        #     u'Tatiana Almeida', u'Celso Alves'
        # ]

    context["nav_active"] = 'chamadas'
    return TemplateResponse(context, template_path='/chamadas/visualizar.html')