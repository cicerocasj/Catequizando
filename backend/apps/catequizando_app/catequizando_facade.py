# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from catequizando_app.catequizando_commands import ListCatequizandoCommand, SaveCatequizandoCommand, UpdateCatequizandoCommand, CatequizandoForm,\
    GetCatequizandoCommand, DeleteCatequizandoCommand


def save_catequizando_cmd(**catequizando_properties):
    """
    Command to save Catequizando entity
    :param catequizando_properties: a dict of properties to save on model
    :return: a Command that save Catequizando, validating and localizing properties received as strings
    """
    return SaveCatequizandoCommand(**catequizando_properties)


def update_catequizando_cmd(catequizando_id, **catequizando_properties):
    """
    Command to update Catequizando entity with id equals 'catequizando_id'
    :param catequizando_properties: a dict of properties to update model
    :return: a Command that update Catequizando, validating and localizing properties received as strings
    """
    return UpdateCatequizandoCommand(catequizando_id, **catequizando_properties)


def list_catequizandos_cmd():
    """
    Command to list Catequizando entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCatequizandoCommand()


def catequizando_form(**kwargs):
    """
    Function to get Catequizando's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CatequizandoForm(**kwargs)


def get_catequizando_cmd(catequizando_id):
    """
    Find catequizando by her id
    :param catequizando_id: the catequizando id
    :return: Command
    """
    return GetCatequizandoCommand(catequizando_id)



def delete_catequizando_cmd(catequizando_id):
    """
    Construct a command to delete a Catequizando
    :param catequizando_id: catequizando's id
    :return: Command
    """
    return DeleteCatequizandoCommand(catequizando_id)

