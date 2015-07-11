# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Chamada(Node):
    encontro = ndb.KeyProperty(required=True)
    data = ndb.StringProperty(required=True)
    turma = ndb.KeyProperty(required=True)
    catequizandos = ndb.StringProperty(required=True)

