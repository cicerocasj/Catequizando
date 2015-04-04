# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from turma_app.turma_commands import ListTurmaCommand, SaveTurmaCommand, UpdateTurmaCommand, TurmaForm,\
    GetTurmaCommand, DeleteTurmaCommand


def save_turma_cmd(**turma_properties):
    """
    Command to save Turma entity
    :param turma_properties: a dict of properties to save on model
    :return: a Command that save Turma, validating and localizing properties received as strings
    """
    return SaveTurmaCommand(**turma_properties)


def update_turma_cmd(turma_id, **turma_properties):
    """
    Command to update Turma entity with id equals 'turma_id'
    :param turma_properties: a dict of properties to update model
    :return: a Command that update Turma, validating and localizing properties received as strings
    """
    return UpdateTurmaCommand(turma_id, **turma_properties)


def list_turmas_cmd():
    """
    Command to list Turma entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListTurmaCommand()


def turma_form(**kwargs):
    """
    Function to get Turma's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return TurmaForm(**kwargs)


def get_turma_cmd(turma_id):
    """
    Find turma by her id
    :param turma_id: the turma id
    :return: Command
    """
    return GetTurmaCommand(turma_id)



def delete_turma_cmd(turma_id):
    """
    Construct a command to delete a Turma
    :param turma_id: turma's id
    :return: Command
    """
    return DeleteTurmaCommand(turma_id)

