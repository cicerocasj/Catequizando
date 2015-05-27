# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from gaepermission.decorator import login_required
from tekton import router
from gaecookie.decorator import no_csrf
from profile_app import profile_facade
from routes import profiles
from tekton.gae.middleware.redirect import RedirectResponse

@login_required
@no_csrf
def index(profile_id):
    profile = profile_facade.get_profile_cmd(profile_id)()
    profile_form = profile_facade.profile_form()
    context = {'save_path': router.to_path(save, profile_id), 'profile': profile_form.fill_with_model(profile)}
    return TemplateResponse(context, 'profiles/profile_form.html')

@login_required
def save(profile_id, **profile_properties):
    cmd = profile_facade.update_profile_cmd(profile_id, **profile_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors, 'profile': profile_properties}

        return TemplateResponse(context, 'profiles/profile_form.html')
    return RedirectResponse(router.to_path(profiles))

