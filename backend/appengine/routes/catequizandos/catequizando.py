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
        context["name"] = u'Osvaldo Brandão'
        context["email"] = u'osvaldinho@gmail.com'
        context["address"] = u'Avenida Juscelino Kubitscheck, 9999, Vila Industrial - São José dos Campos'
        context["phone"] = u'3333-3333'
        context["cellphone"] = u'98888-8888'
        context["avatar"] = u'avatar3.jpg'
        context["group"] = {
            'type': 'crisma 3',
            'day': 'quarta',
            'hours': '19:00 - 20:00',
            'local': u'paróquia',
            'catechized': 16,
        }
    context["nav_active"] = 'catequizandos'
    context["responsible_1"] = {'name': u'José Carlos', 'phone': '3333-3333'}
    context["responsible_2"] = {'name': u'Maria das Dores', 'phone': '3333-3333'}
    return TemplateResponse(context, template_path='/catequizandos/catequizando.html')