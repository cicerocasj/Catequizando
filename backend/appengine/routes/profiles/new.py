# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_required
from gaepermission import facade
from tekton import router
from gaecookie.decorator import no_csrf
from profile_app import profile_facade
from routes import profiles
from tekton.gae.middleware.redirect import RedirectResponse


@login_required
@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)}, 'profiles/profile_form.html')

@login_required
def save(**profile_properties):

    cmd = profile_facade.save_profile_cmd(**profile_properties)
    try:
        p = cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'profile': profile_properties}

        return TemplateResponse(context, 'profiles/profile_form.html')
    s = facade.save_user_cmd(p.email, p.name, p.groups)
    return RedirectResponse(router.to_path(profiles))

