# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from catequizando_app import catequizando_facade
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from routes import catequizandos
from routes.catequizandos import download
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse
from tekton.router import to_path
from turma_app.turma_model import Turma


def index(_handler, **catequizando_properties):
    if catequizando_properties.get("files[]"):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequizando_properties["avatar"] = avatar
        # turma = Turma.get_by_id(5207287069147136)
        # catequizando_properties["turma"] = turma.key
    catequizando_properties.pop("files", None)
    cmd = catequizando_facade.save_catequizando_cmd(**catequizando_properties)
    try:
        a = cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'catechized': catequizando_properties}
        return TemplateResponse(context, '/catequizandos/catequizando.html')
    return RedirectResponse(router.to_path(catequizandos))