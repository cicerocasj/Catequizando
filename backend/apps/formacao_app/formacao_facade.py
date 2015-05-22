# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from formacao_app.formacao_commands import ListFormacaoCommand, SaveFormacaoCommand, UpdateFormacaoCommand, FormacaoForm,\
    GetFormacaoCommand, DeleteFormacaoCommand


def save_formacao_cmd(**formacao_properties):
    """
    Command to save Formacao entity
    :param formacao_properties: a dict of properties to save on model
    :return: a Command that save Formacao, validating and localizing properties received as strings
    """
    return SaveFormacaoCommand(**formacao_properties)


def update_formacao_cmd(formacao_id, **formacao_properties):
    """
    Command to update Formacao entity with id equals 'formacao_id'
    :param formacao_properties: a dict of properties to update model
    :return: a Command that update Formacao, validating and localizing properties received as strings
    """
    return UpdateFormacaoCommand(formacao_id, **formacao_properties)


def list_formacaos_cmd():
    """
    Command to list Formacao entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListFormacaoCommand()


def formacao_form(**kwargs):
    """
    Function to get Formacao's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return FormacaoForm(**kwargs)


def get_formacao_cmd(formacao_id):
    """
    Find formacao by her id
    :param formacao_id: the formacao id
    :return: Command
    """
    return GetFormacaoCommand(formacao_id)



def delete_formacao_cmd(formacao_id):
    """
    Construct a command to delete a Formacao
    :param formacao_id: formacao's id
    :return: Command
    """
    return DeleteFormacaoCommand(formacao_id)

