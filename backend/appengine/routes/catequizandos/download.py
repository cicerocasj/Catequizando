# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, login_required
from permission_app.model import validate_permission, COORDENADOR


@login_required
@no_csrf
def index(_logged_user, _handler, blob_key):
    access_denid = validate_permission(COORDENADOR, _logged_user)
    if access_denid:
        return access_denid
    _handler.send_blob(blob_key)