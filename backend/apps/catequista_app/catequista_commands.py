# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from catequista_app.catequista_model import Catequista



class CatequistaSaveForm(ModelForm):
    """
    Form used to save and update Catequista
    """
    _model_class = Catequista
    _include = [
        Catequista.name,
        Catequista.email,
        Catequista.phone,
        Catequista.cellphone,
        Catequista.address,
        Catequista.avatar,
        Catequista.username,
        Catequista.password,
        Catequista.groups
    ]


class CatequistaForm(ModelForm):
    """
    Form used to expose Catequista's properties for list or json
    """
    _model_class = Catequista


class GetCatequistaCommand(NodeSearch):
    _model_class = Catequista


class DeleteCatequistaCommand(DeleteNode):
    _model_class = Catequista


class SaveCatequistaCommand(SaveCommand):
    _model_form_class = CatequistaSaveForm


class UpdateCatequistaCommand(UpdateNode):
    _model_form_class = CatequistaSaveForm


class ListCatequistaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCatequistaCommand, self).__init__(Catequista.query_by_creation())

