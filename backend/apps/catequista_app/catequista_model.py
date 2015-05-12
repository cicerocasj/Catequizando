# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.business_base import DeleteArcs
from gaegraph.model import Node
from gaegraph.model import Arc


class Catequista(Node):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=False)
    phone = ndb.StringProperty(required=False)
    cellphone = ndb.StringProperty(required=False)
    address = ndb.StringProperty(required=False)
    avatar = ndb.StringProperty(required=False)


class TurmaCatequista(Arc):
    # turma
    origin = ndb.KeyProperty()
    # catequista
    destination = ndb.KeyProperty(Catequista)


class DeletarTurmaCatequista(DeleteArcs):
    arc_class = TurmaCatequista

    def __init__(self, origin=None, destination=None):
        super(DeletarTurmaCatequista, self).__init__(origin, destination)


class DeletarTurmaForever(DeleteArcs):
    arc_class = TurmaCatequista

    def __init__(self, origin=None):
        super(DeletarTurmaForever, self).__init__(origin)