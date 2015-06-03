# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from user_app import user_facade
from routes import users
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index(user_id):
    user = user_facade.get_user_cmd(user_id)()
    user_form = user_facade.user_form()
    context = {'save_path': router.to_path(save, user_id), 'user': user_form.fill_with_model(user)}
    return TemplateResponse(context, 'users/user_form.html')


def save(user_id, **user_properties):
    cmd = user_facade.update_user_cmd(user_id, **user_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'user': user_properties}

        return TemplateResponse(context, 'users/user_form.html')
    return RedirectResponse(router.to_path(users))

