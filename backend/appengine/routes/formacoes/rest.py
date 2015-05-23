# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.json_middleware import JsonResponse
from formacao_app import formacao_facade


@login_not_required
def index():
    cmd = formacao_facade.list_formacaos_cmd()
    formacao_list = cmd()
    formacao_form = formacao_facade.formacao_form()
    formacao_dcts = [formacao_form.fill_with_model(m) for m in formacao_list]
    return JsonResponse(formacao_dcts)


@login_not_required
def new(_resp, **formacao_properties):
    cmd = formacao_facade.save_formacao_cmd(**formacao_properties)
    return _save_or_update_json_response(cmd, _resp)


@login_not_required
def edit(_resp, id, **formacao_properties):
    cmd = formacao_facade.update_formacao_cmd(id, **formacao_properties)
    return _save_or_update_json_response(cmd, _resp)


@login_not_required
def delete(_resp, id):
    cmd = formacao_facade.delete_formacao_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


@login_not_required
def _save_or_update_json_response(cmd, _resp):
    try:
        formacao = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    formacao_form = formacao_facade.formacao_form()
    return JsonResponse(formacao_form.fill_with_model(formacao))

