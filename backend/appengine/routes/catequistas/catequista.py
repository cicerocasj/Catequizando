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
        context["name"] = u'Cícero Alves dos Santos Junior'
        context["email"] = u'cicerocasj@gmail.com'
        context["address"] = u'Avenida Juscelino Kubitscheck, 9999, Vila Industrial - São José dos Campos'
        context["phone"] = u'3333-3333'
        context["cellphone"] = u'98888-8888'
        context["avatar"] = u'avatar1.jpg'
        context["groups"] = [
            {'type': 'crisma 3', 'day': 'quarta', 'hours': '19:00 - 20:00', 'local': u'paróquia', 'catechized': 16}
        ]

        if key_id == 2:
            context["id"] = id
            context["name"] = u'Maria Aparecida da Silva'
            context["email"] = u'maria@outlook.com'
            context["address"] = u'Rua Ortolandia, 9999, Vista Linda - São José dos Campos'
            context["phone"] = u'3333-3333'
            context["cellphone"] = u'98888-8888'
            context["avatar"] = u'avatar2.jpg'
            context["groups"] = [
                {'type': 'crisma 2', 'day': u'terça', 'hours': '19:00 - 20:00', 'local': u'paróquia', 'catechized': 10},
                {'type': 'eucaristia 1', 'day': u'sábado', 'hours': '9:00 - 10:30', 'local': u'Capela São Marcos', 'catechized': 22}
            ]
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/catequista.html')