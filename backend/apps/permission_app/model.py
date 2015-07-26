# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton.gae.middleware.redirect import RedirectResponse

ADMIN = 'ADMIN'
CATEQUISTA = 'CATEQUISTA'
COORDENADOR = 'COORDENADOR'
CATEQUIZANDO = 'CATEQUIZANDO'
COMUM = 'COMUM'

ALL_PERMISSIONS_LIST = [ADMIN, CATEQUISTA, COORDENADOR, CATEQUIZANDO, COMUM]


def validate_permission(permission, user):
    if permission == ADMIN:
        return False
    groups = user.groups if hasattr(user, 'groups') else []
    print permission not in groups
    if permission not in groups:
        return RedirectResponse('/erro')