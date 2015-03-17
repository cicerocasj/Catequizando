# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from noticia_app import noticia_facade


def index():
    cmd = noticia_facade.list_noticias_cmd()
    noticia_list = cmd()
    noticia_form = noticia_facade.noticia_form()
    noticia_dcts = [noticia_form.fill_with_model(m) for m in noticia_list]
    return JsonResponse(noticia_dcts)


def new(_resp, **noticia_properties):
    cmd = noticia_facade.save_noticia_cmd(**noticia_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **noticia_properties):
    cmd = noticia_facade.update_noticia_cmd(id, **noticia_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = noticia_facade.delete_noticia_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        noticia = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    noticia_form = noticia_facade.noticia_form()
    return JsonResponse(noticia_form.fill_with_model(noticia))

