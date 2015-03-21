# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequizando_app import catequizando_commands, catequizando_facade
from catequizando_app.catequizando_model import Catequizando
from gaebusiness.business import CommandExecutionException
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from routes import catequizandos
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catechized"] = Catequizando.get_by_id(key_id)

    context["nav_active"] = 'catequizandos'
    context["save_path"] = router.to_path(save)
    return TemplateResponse(context, template_path='/catequizandos/catequizando.html')


def save(**catequizando_properties):
    cmd = catequizando_facade.save_catequizando_cmd(**catequizando_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catechized': catequizando_properties}
        return TemplateResponse(context, '/catequizandos/catequizando.html')
    return RedirectResponse(router.to_path(catequizandos))