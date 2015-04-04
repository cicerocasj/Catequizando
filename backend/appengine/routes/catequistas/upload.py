# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app import catequista_facade
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from routes import catequistas
from routes.catequistas import download
from tekton import router
from tekton.router import to_path
from tekton.gae.middleware.redirect import RedirectResponse


def index(_handler, **catequistas_properties):
    blob_infos = _handler.get_uploads("files[]")
    blob_key = blob_infos[0].key()
    avatar = to_path(download, blob_key)
    catequistas_properties['avatar'] = avatar
    catequistas_properties.pop("files", None)
    cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {
            'errors': cmd.erros,
            'catequista': catequistas_properties
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    return RedirectResponse(router.to_path(catequistas))