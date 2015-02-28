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
    context["nav_active"] = 'catequista'
    return TemplateResponse(context, template_path='/catequista/catequista.html')