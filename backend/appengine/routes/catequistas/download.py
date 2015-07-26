# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from permission_app.model import validate_permission, ADMIN


@login_not_required
@no_csrf
def index(_logged_user, _handler, blob_key):
    access_invalid = validate_permission(ADMIN, _logged_user)
    if access_invalid:
        return access_invalid
    _handler.send_blob(blob_key)