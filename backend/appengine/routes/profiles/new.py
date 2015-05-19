# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from profile_app import profile_facade
from routes import profiles
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'profiles/profile_form.html')


def save(**profile_properties):
    cmd = profile_facade.save_profile_cmd(**profile_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'profile': profile_properties}

        return TemplateResponse(context, 'profiles/profile_form.html')
    return RedirectResponse(router.to_path(profiles))

