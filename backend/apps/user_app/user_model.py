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
        if username:
            users = User.query(User.username==username).fetch()
            return False if users else True
        return False

    @staticmethod
    def alter_user(username):
        if username:
            users = User.query(User.username==username).fetch()
            return False if len(users) > 1 else True
        return False

    @staticmethod
    def is_unique_email(email):
        if email:
            users = User.query(User.email==email).fetch()
            return False if users else True
        return False

    @staticmethod
    def alter_user_email(email):
        if email:
            users = User.query(User.email==email).fetch()
            return False if len(users) > 1 else True
        return False