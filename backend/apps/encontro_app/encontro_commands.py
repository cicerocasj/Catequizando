# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from encontro_app.encontro_model import Encontro



class EncontroSaveForm(ModelForm):
    """
    Form used to save and update Encontro
    """
    _model_class = Encontro
    _include = [Encontro.content, 
                Encontro.link, 
                Encontro.title]


class EncontroForm(ModelForm):
    """
    Form used to expose Encontro's properties for list or json
    """
    _model_class = Encontro


class GetEncontroCommand(NodeSearch):
    _model_class = Encontro


class DeleteEncontroCommand(DeleteNode):
    _model_class = Encontro


class SaveEncontroCommand(SaveCommand):
    _model_form_class = EncontroSaveForm


class UpdateEncontroCommand(UpdateNode):
    _model_form_class = EncontroSaveForm


class ListEncontroCommand(ModelSearchCommand):
    def __init__(self):
        super(ListEncontroCommand, self).__init__(Encontro.query_by_creation())

