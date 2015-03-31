# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from catequizando_app.catequizando_model import Catequizando


class CatequizandoSaveForm(ModelForm):
    """
    Form used to save and update Catequizando
    """
    _model_class = Catequizando
    _include = [
        Catequizando.name,
        Catequizando.email,
        Catequizando.address,
        Catequizando.phone,
        Catequizando.cellphone,
        Catequizando.avatar,
        Catequizando.group,
        Catequizando.responsible_1_name,
        Catequizando.responsible_1_phone,
        Catequizando.responsible_2_name,
        Catequizando.responsible_2_phone,
    ]


class CatequizandoForm(ModelForm):
    """
    Form used to expose Catequizando's properties for list or json
    """
    _model_class = Catequizando


class GetCatequizandoCommand(NodeSearch):
    _model_class = Catequizando


class DeleteCatequizandoCommand(DeleteNode):
    _model_class = Catequizando


class SaveCatequizandoCommand(SaveCommand):
    _model_form_class = CatequizandoSaveForm


class UpdateCatequizandoCommand(UpdateNode):
    _model_form_class = CatequizandoSaveForm


class ListCatequizandoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListCatequizandoCommand, self).__init__(Catequizando.query_by_creation())

