# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api import users
from gaecookie.decorator import no_csrf
from gaepermission import facade
from gaepermission.base_commands import log_main_user_in
from gaepermission.decorator import login_not_required
from profile_app.profile_model import Profile
from tekton import router
from config.template_middleware import TemplateResponse
from routes.login import google, facebook, auth
from routes.login.passwordless import send_email
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index(ret_path='/'):
    g_path = router.to_path(google.index, ret_path=ret_path)
    # {'sidebar_small': True}
    dct = {'login_google_path': users.create_login_url(g_path),
           'login_passwordless_path': router.to_path(send_email, ret_path=ret_path),
           'login_facebook_path': router.to_path(facebook.index, ret_path=ret_path),
           'custom_login': router.to_path(auth),
           'faceapp': facade.get_facebook_app_data().execute().result,
           'hide_navbar': True}
    return TemplateResponse(dct)
