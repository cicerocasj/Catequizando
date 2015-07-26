# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions, login_required
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO


@no_csrf
@login_required
def index():
    return TemplateResponse()

