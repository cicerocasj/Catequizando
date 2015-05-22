# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from formacao_app import formacao_facade


def index():
    cmd = formacao_facade.list_formacaos_cmd()
    formacao_list = cmd()
    formacao_form = formacao_facade.formacao_form()
    formacao_dcts = [formacao_form.fill_with_model(m) for m in formacao_list]
    return JsonResponse(formacao_dcts)


def new(_resp, **formacao_properties):
    cmd = formacao_facade.save_formacao_cmd(**formacao_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **formacao_properties):
    cmd = formacao_facade.update_formacao_cmd(id, **formacao_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = formacao_facade.delete_formacao_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        formacao = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    formacao_form = formacao_facade.formacao_form()
    return JsonResponse(formacao_form.fill_with_model(formacao))

