# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from catequista_app.catequista_model import Catequista
from gaegraph.model import Node
from gaeforms.ndb import property
from gaepermission.model import MainUser


class Profile(Node):
    user = ndb.KeyProperty(MainUser)
    tipo = ndb.KeyProperty(Catequista)

