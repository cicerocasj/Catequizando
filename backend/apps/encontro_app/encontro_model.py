# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node


class Encontro(Node):
    title = ndb.StringProperty(required=True)
    content = ndb.TextProperty(required=True)
    objetive = ndb.TextProperty(required=True)
