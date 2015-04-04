# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node


class Turma(Node):

    choice_day = (
        'Segunda-feira',
        'Terça-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sábado',
        'Domingo'
    )

    choice_type = (
        "Pré catequese",
        "Eucaristia 1",
        "Eucaristia 2",
        "Eucaristia 3",
        "Crisma 1",
        "Crisma 2",
        "Crisma 3"
    )

    type = ndb.StringProperty(required=True, choices=choice_type)
    initial_hour = ndb.StringProperty(required=True)
    end_hour = ndb.StringProperty(required=True)
    local = ndb.StringProperty(required=True)
    day = ndb.StringProperty(required=True, choices=choice_day)