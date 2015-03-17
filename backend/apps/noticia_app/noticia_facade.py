# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from noticia_app.noticia_commands import ListNoticiaCommand, SaveNoticiaCommand, UpdateNoticiaCommand, NoticiaForm,\
    GetNoticiaCommand, DeleteNoticiaCommand


def save_noticia_cmd(**noticia_properties):
    """
    Command to save Noticia entity
    :param noticia_properties: a dict of properties to save on model
    :return: a Command that save Noticia, validating and localizing properties received as strings
    """
    return SaveNoticiaCommand(**noticia_properties)


def update_noticia_cmd(noticia_id, **noticia_properties):
    """
    Command to update Noticia entity with id equals 'noticia_id'
    :param noticia_properties: a dict of properties to update model
    :return: a Command that update Noticia, validating and localizing properties received as strings
    """
    return UpdateNoticiaCommand(noticia_id, **noticia_properties)


def list_noticias_cmd():
    """
    Command to list Noticia entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListNoticiaCommand()


def noticia_form(**kwargs):
    """
    Function to get Noticia's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return NoticiaForm(**kwargs)


def get_noticia_cmd(noticia_id):
    """
    Find noticia by her id
    :param noticia_id: the noticia id
    :return: Command
    """
    return GetNoticiaCommand(noticia_id)



def delete_noticia_cmd(noticia_id):
    """
    Construct a command to delete a Noticia
    :param noticia_id: noticia's id
    :return: Command
    """
    return DeleteNoticiaCommand(noticia_id)

