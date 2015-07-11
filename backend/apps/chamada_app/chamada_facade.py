# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from chamada_app.chamada_commands import ListChamadaCommand, SaveChamadaCommand, UpdateChamadaCommand, ChamadaForm,\
    GetChamadaCommand, DeleteChamadaCommand


def save_chamada_cmd(**chamada_properties):
    """
    Command to save Chamada entity
    :param chamada_properties: a dict of properties to save on model
    :return: a Command that save Chamada, validating and localizing properties received as strings
    """
    return SaveChamadaCommand(**chamada_properties)


def update_chamada_cmd(chamada_id, **chamada_properties):
    """
    Command to update Chamada entity with id equals 'chamada_id'
    :param chamada_properties: a dict of properties to update model
    :return: a Command that update Chamada, validating and localizing properties received as strings
    """
    return UpdateChamadaCommand(chamada_id, **chamada_properties)


def list_chamadas_cmd():
    """
    Command to list Chamada entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListChamadaCommand()


def chamada_form(**kwargs):
    """
    Function to get Chamada's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ChamadaForm(**kwargs)


def get_chamada_cmd(chamada_id):
    """
    Find chamada by her id
    :param chamada_id: the chamada id
    :return: Command
    """
    return GetChamadaCommand(chamada_id)



def delete_chamada_cmd(chamada_id):
    """
    Construct a command to delete a Chamada
    :param chamada_id: chamada's id
    :return: Command
    """
    return DeleteChamadaCommand(chamada_id)

