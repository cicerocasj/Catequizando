# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from encontro_app.encontro_commands import ListEncontroCommand, SaveEncontroCommand, UpdateEncontroCommand, EncontroForm,\
    GetEncontroCommand, DeleteEncontroCommand


def save_encontro_cmd(**encontro_properties):
    """
    Command to save Encontro entity
    :param encontro_properties: a dict of properties to save on model
    :return: a Command that save Encontro, validating and localizing properties received as strings
    """
    return SaveEncontroCommand(**encontro_properties)


def update_encontro_cmd(encontro_id, **encontro_properties):
    """
    Command to update Encontro entity with id equals 'encontro_id'
    :param encontro_properties: a dict of properties to update model
    :return: a Command that update Encontro, validating and localizing properties received as strings
    """
    return UpdateEncontroCommand(encontro_id, **encontro_properties)


def list_encontros_cmd():
    """
    Command to list Encontro entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListEncontroCommand()


def encontro_form(**kwargs):
    """
    Function to get Encontro's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return EncontroForm(**kwargs)


def get_encontro_cmd(encontro_id):
    """
    Find encontro by her id
    :param encontro_id: the encontro id
    :return: Command
    """
    return GetEncontroCommand(encontro_id)



def delete_encontro_cmd(encontro_id):
    """
    Construct a command to delete a Encontro
    :param encontro_id: encontro's id
    :return: Command
    """
    return DeleteEncontroCommand(encontro_id)

