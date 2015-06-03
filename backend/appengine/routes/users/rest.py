# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from user_app import user_facade


def index():
    cmd = user_facade.list_users_cmd()
    user_list = cmd()
    user_form = user_facade.user_form()
    user_dcts = [user_form.fill_with_model(m) for m in user_list]
    return JsonResponse(user_dcts)


def new(_resp, **user_properties):
    cmd = user_facade.save_user_cmd(**user_properties)
    return _save_or_update_json_response(cmd, _resp)


def edit(_resp, id, **user_properties):
    cmd = user_facade.update_user_cmd(id, **user_properties)
    return _save_or_update_json_response(cmd, _resp)


def delete(_resp, id):
    cmd = user_facade.delete_user_cmd(id)
    try:
        cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)


def _save_or_update_json_response(cmd, _resp):
    try:
        user = cmd()
    except CommandExecutionException:
        _resp.status_code = 500
        return JsonResponse(cmd.errors)
    user_form = user_facade.user_form()
    return JsonResponse(user_form.fill_with_model(user))

