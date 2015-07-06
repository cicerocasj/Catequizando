# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from turma_app.turma_model import Turma
from user_app.user_model import User


class Catequizando(User):
    address = ndb.StringProperty(required=False)
    phone = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    cellphone = ndb.StringProperty(required=False)
    avatar = ndb.StringProperty(required=False)
    group = ndb.StringProperty(required=False)
    responsible_1_name = ndb.StringProperty(required=False)
    responsible_1_phone = ndb.StringProperty(required=False)
    responsible_2_name = ndb.StringProperty(required=False)
    responsible_2_phone = ndb.StringProperty(required=False)
    turma = ndb.KeyProperty(Turma, required=False)


# name
# email
# address
# phone
# cellphone
# avatar
# group
# responsible_1
# responsible_2