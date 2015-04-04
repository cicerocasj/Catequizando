# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Catequista(Node):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=False)
    phone = ndb.StringProperty(required=False)
    cellphone = ndb.StringProperty(required=False)
    address = ndb.StringProperty(required=False)
    avatar = ndb.StringProperty(required=False)
