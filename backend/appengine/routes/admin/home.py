# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from config.template_middleware import TemplateResponse
from tekton import router
from routes.login import passwordless, facebook
from routes.permission import home as permission_home, admin
from gaepermission.decorator import login_required
from permission_app.model import ADMIN, validate_permission


@login_required
@no_csrf
def index(_logged_user):
    access_denid = validate_permission(ADMIN, _logged_user)
    if access_denid:
        return access_denid
    return TemplateResponse({'security_table_path': router.to_path(permission_home.index),
                             'permission_admin_path': router.to_path(admin),
                             'passwordless_admin_path': router.to_path(passwordless.form),
                             'facebook_admin_path': router.to_path(facebook.form)})
