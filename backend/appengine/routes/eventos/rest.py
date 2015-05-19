# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from evento_app import evento_facade


def index():
    cmd = evento_facade.list_eventos_cmd()
    evento_list = cmd()
    evento_form = evento_facade.evento_form()
    evento_dcts = [evento_form.fill_with_model(m) for m in evento_list]
    return JsonResponse(evento_dcts)


def new(_resp, **evento_properties):
    cmd = evento_facade.save_evento_cmd(**evento_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **evento_properties):
    cmd = evento_facade.update_evento_cmd(id, **evento_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = evento_facade.delete_evento_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        evento = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    evento_form = evento_facade.evento_form()
    return JsonResponse(evento_form.fill_with_model(evento))

