# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequizando_app.catequizando_model import Catequizando
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from turma_app.turma_model import Turma


class TurmaSaveForm(ModelForm):
    """
    Form used to save and update Turma
    """

    _model_class = Turma
    _include = [
        Turma.type,
        Turma.initial_hour,
        Turma.end_hour,
        Turma.local,
        Turma.day,
    ]


class TurmaForm(ModelForm):
    """
    Form used to expose Turma's properties for list or json
    """
    _model_class = Turma


class GetTurmaCommand(NodeSearch):
    _model_class = Turma


class DeleteTurmaCommand(DeleteNode):
    _model_class = Turma


class SaveTurmaCommand(SaveCommand):
    _model_form_class = TurmaSaveForm


class UpdateTurmaCommand(UpdateNode):
    _model_form_class = TurmaSaveForm


class ListTurmaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListTurmaCommand, self).__init__(Turma.query_by_creation())


def choice_catequizandos():
    query = Catequizando.query()
    return query.fetch()


def catequizandos(turma_key):
    return Catequizando.query(Catequizando.turma==turma_key).fetch()