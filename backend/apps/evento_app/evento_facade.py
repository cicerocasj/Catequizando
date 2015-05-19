# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from evento_app.evento_commands import ListEventoCommand, SaveEventoCommand, UpdateEventoCommand, EventoForm,\
    GetEventoCommand, DeleteEventoCommand


def save_evento_cmd(**evento_properties):
    """
    Command to save Evento entity
    :param evento_properties: a dict of properties to save on model
    :return: a Command that save Evento, validating and localizing properties received as strings
    """
    return SaveEventoCommand(**evento_properties)


def update_evento_cmd(evento_id, **evento_properties):
    """
    Command to update Evento entity with id equals 'evento_id'
    :param evento_properties: a dict of properties to update model
    :return: a Command that update Evento, validating and localizing properties received as strings
    """
    return UpdateEventoCommand(evento_id, **evento_properties)


def list_eventos_cmd():
    """
    Command to list Evento entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListEventoCommand()


def evento_form(**kwargs):
    """
    Function to get Evento's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return EventoForm(**kwargs)


def get_evento_cmd(evento_id):
    """
    Find evento by her id
    :param evento_id: the evento id
    :return: Command
    """
    return GetEventoCommand(evento_id)



def delete_evento_cmd(evento_id):
    """
    Construct a command to delete a Evento
    :param evento_id: evento's id
    :return: Command
    """
    return DeleteEventoCommand(evento_id)

