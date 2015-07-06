# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property
from gaepermission.model import MainUser


class User(MainUser):
    username = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

    @staticmethod
    def is_unique(username):
        users = User.query(User.username==username).fetch()
        return False if users else True