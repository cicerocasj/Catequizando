# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaepermission.decorator import login_required
from tekton import router
from gaecookie.decorator import no_csrf
from profile_app import profile_facade
from routes.profiles import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@login_required
@no_csrf
def index():
    cmd = profile_facade.list_profiles_cmd()
    profiles = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    profile_form = profile_facade.profile_form()

    def localize_profile(profile):
        profile_dct = profile_form.fill_with_model(profile)
        profile_dct['edit_path'] = router.to_path(edit_path, profile_dct['id'])
        profile_dct['delete_path'] = router.to_path(delete_path, profile_dct['id'])
        return profile_dct

    localized_profiles = [localize_profile(profile) for profile in profiles]
    context = {'profiles': localized_profiles,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'profiles/profile_home.html')


def delete(profile_id):
    profile_facade.delete_profile_cmd(profile_id)()
    return RedirectResponse(router.to_path(index))

