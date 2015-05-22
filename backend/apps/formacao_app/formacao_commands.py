# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from formacao_app.formacao_model import Formacao



class FormacaoSaveForm(ModelForm):
    """
    Form used to save and update Formacao
    """
    _model_class = Formacao
    _include = [Formacao.titulo, 
                Formacao.data, 
                Formacao.conteudo]


class FormacaoForm(ModelForm):
    """
    Form used to expose Formacao's properties for list or json
    """
    _model_class = Formacao


class GetFormacaoCommand(NodeSearch):
    _model_class = Formacao


class DeleteFormacaoCommand(DeleteNode):
    _model_class = Formacao


class SaveFormacaoCommand(SaveCommand):
    _model_form_class = FormacaoSaveForm


class UpdateFormacaoCommand(UpdateNode):
    _model_form_class = FormacaoSaveForm


class ListFormacaoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListFormacaoCommand, self).__init__(Formacao.query_by_creation())

