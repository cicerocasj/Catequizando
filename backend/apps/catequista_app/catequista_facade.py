# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from catequista_app.catequista_commands import ListCatequistaCommand, SaveCatequistaCommand, UpdateCatequistaCommand, CatequistaForm,\
    GetCatequistaCommand, DeleteCatequistaCommand


def save_catequista_cmd(**catequista_properties):
    """
    Command to save Catequista entity
    :param catequista_properties: a dict of properties to save on model
    :return: a Command that save Catequista, validating and localizing properties received as strings
    """
    return SaveCatequistaCommand(**catequista_properties)


def update_catequista_cmd(catequista_id, **catequista_properties):
    """
    Command to update Catequista entity with id equals 'catequista_id'
    :param catequista_properties: a dict of properties to update model
    :return: a Command that update Catequista, validating and localizing properties received as strings
    """
    return UpdateCatequistaCommand(catequista_id, **catequista_properties)


def list_catequistas_cmd():
    """
    Command to list Catequista entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListCatequistaCommand()


def catequista_form(**kwargs):
    """
    Function to get Catequista's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return CatequistaForm(**kwargs)


def get_catequista_cmd(catequista_id):
    """
    Find catequista by her id
    :param catequista_id: the catequista id
    :return: Command
    """
    return GetCatequistaCommand(catequista_id)



def delete_catequista_cmd(catequista_id):
    """
    Construct a command to delete a Catequista
    :param catequista_id: catequista's id
    :return: Command
    """
    return DeleteCatequistaCommand(catequista_id)

