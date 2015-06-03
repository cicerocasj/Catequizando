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
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'users/user_form.html')


def save(**user_properties):
    cmd = user_facade.save_user_cmd(**user_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'user': user_properties}

        return TemplateResponse(context, 'users/user_form.html')
    return RedirectResponse(router.to_path(users))

