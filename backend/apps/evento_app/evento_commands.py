# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from evento_app.evento_model import Evento



class EventoSaveForm(ModelForm):
    """
    Form used to save and update Evento
    """
    _model_class = Evento
    _include = [Evento.start, 
                Evento.end, 
                Evento.description, 
                Evento.title]


class EventoForm(ModelForm):
    """
    Form used to expose Evento's properties for list or json
    """
    _model_class = Evento


class GetEventoCommand(NodeSearch):
    _model_class = Evento


class DeleteEventoCommand(DeleteNode):
    _model_class = Evento


class SaveEventoCommand(SaveCommand):
    _model_form_class = EventoSaveForm


class UpdateEventoCommand(UpdateNode):
    _model_form_class = EventoSaveForm


class ListEventoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListEventoCommand, self).__init__(Evento.query_by_creation())

