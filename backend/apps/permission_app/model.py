# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from tekton.gae.middleware.redirect import RedirectResponse

ADMIN = 'ADMIN'
CATEQUISTA = 'CATEQUISTA'
COORDENADOR = 'COORDENADOR'
CATEQUIZANDO = 'CATEQUIZANDO'
COMUM = 'COMUM'

ALL_PERMISSIONS_LIST = [ADMIN, CATEQUIZANDO, CATEQUISTA, COORDENADOR, COMUM]


def validate_permission(permission, user):
    if permission == ADMIN:
        return False
    groups = user.groups if hasattr(user, 'groups') else []
    print permission not in groups
    if permission not in groups:
        return RedirectResponse('/erro')


def set_permission(permission):
    permissions = []
    if permission == COORDENADOR:
        permissions.append(COORDENADOR)
        permissions.append(CATEQUISTA)
        permissions.append(CATEQUIZANDO)
        permissions.append(COMUM)
    elif permission == CATEQUISTA:
        permissions.append(CATEQUISTA)
        permissions.append(CATEQUIZANDO)
        permissions.append(COMUM)
    elif permission == CATEQUIZANDO:
        permissions.append(CATEQUIZANDO)
        permissions.append(COMUM)
    else:
        permissions.append(COMUM)
    return permissions