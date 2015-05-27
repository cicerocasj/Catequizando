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
from routes.login import google, facebook
from routes.login.passwordless import send_email
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index(_resp, **data):
    main_user = Profile.query().fetch()[0] if Profile.query().count() else None
    log_main_user_in(main_user, _resp, 'userck')
    return RedirectResponse('/admin')