# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from catequista_app.catequista_model import TurmaCatequista, Catequista
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from chamada_app.chamada_model import Chamada
from turma_app.turma_model import Turma


class ChamadaSaveForm(ModelForm):
    """
    Form used to save and update Chamada
    """
    _model_class = Chamada
    _include = [Chamada.encontro, 
                Chamada.data, 
                Chamada.turma,
                Chamada.catequizandos]


class ChamadaForm(ModelForm):
    """
    Form used to expose Chamada's properties for list or json
    """
    _model_class = Chamada


class GetChamadaCommand(NodeSearch):
    _model_class = Chamada


class DeleteChamadaCommand(DeleteNode):
    _model_class = Chamada


class SaveChamadaCommand(SaveCommand):
    _model_form_class = ChamadaSaveForm


class UpdateChamadaCommand(UpdateNode):
    _model_form_class = ChamadaSaveForm


class ListChamadaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListChamadaCommand, self).__init__(Chamada.query_by_creation())

def choice_catequizandos():
    # query = Catequizando.query()
    # return query.fetch()
    pass

def choice_turmas(user, all):
    if all:
        turma_cats = TurmaCatequista.query().fetch()
    else:
        turma_cats = TurmaCatequista.query(TurmaCatequista.destination==user.key).fetch()
    turmas = []
    for turma_cat in turma_cats:
        turma = Turma.get_by_id(turma_cat.origin.id())
        catequista_name = Catequista.get_by_id(turma_cat.destination.id()).name
        label = "{} - {} {}".format(turma.type, turma.day, turma.initial_hour)
        turmas.append({'id': turma.key.id(), 'name': label, 'catequista': catequista_name})
    return turmas