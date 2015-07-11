# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from chamada_app import chamada_facade


def index():
    cmd = chamada_facade.list_chamadas_cmd()
    chamada_list = cmd()
    chamada_form = chamada_facade.chamada_form()
    chamada_dcts = [chamada_form.fill_with_model(m) for m in chamada_list]
    return JsonResponse(chamada_dcts)


def new(_resp, **chamada_properties):
    cmd = chamada_facade.save_chamada_cmd(**chamada_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **chamada_properties):
    cmd = chamada_facade.update_chamada_cmd(id, **chamada_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = chamada_facade.delete_chamada_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        chamada = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    chamada_form = chamada_facade.chamada_form()
    return JsonResponse(chamada_form.fill_with_model(chamada))

