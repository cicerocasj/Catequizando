# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from noticia_app.noticia_model import Noticia



class NoticiaSaveForm(ModelForm):
    """
    Form used to save and update Noticia
    """
    _model_class = Noticia
    _include = [Noticia.content, 
                Noticia.link, 
                Noticia.title]


class NoticiaForm(ModelForm):
    """
    Form used to expose Noticia's properties for list or json
    """
    _model_class = Noticia


class GetNoticiaCommand(NodeSearch):
    _model_class = Noticia


class DeleteNoticiaCommand(DeleteNode):
    _model_class = Noticia


class SaveNoticiaCommand(SaveCommand):
    _model_form_class = NoticiaSaveForm


class UpdateNoticiaCommand(UpdateNode):
    _model_form_class = NoticiaSaveForm


class ListNoticiaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListNoticiaCommand, self).__init__(Noticia.query_by_creation())

