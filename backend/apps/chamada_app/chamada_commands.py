# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from chamada_app.chamada_model import Chamada



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
    query = Catequizando.query()
    return query.fetch()