# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from user_app.user_commands import ListUserCommand, SaveUserCommand, UpdateUserCommand, UserForm,\
    GetUserCommand, DeleteUserCommand


def save_user_cmd(**user_properties):
    """
    Command to save User entity
    :param user_properties: a dict of properties to save on model
    :return: a Command that save User, validating and localizing properties received as strings
    """
    return SaveUserCommand(**user_properties)


def update_user_cmd(user_id, **user_properties):
    """
    Command to update User entity with id equals 'user_id'
    :param user_properties: a dict of properties to update model
    :return: a Command that update User, validating and localizing properties received as strings
    """
    return UpdateUserCommand(user_id, **user_properties)


def list_users_cmd():
    """
    Command to list User entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListUserCommand()


def user_form(**kwargs):
    """
    Function to get User's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return UserForm(**kwargs)


def get_user_cmd(user_id):
    """
    Find user by her id
    :param user_id: the user id
    :return: Command
    """
    return GetUserCommand(user_id)



def delete_user_cmd(user_id):
    """
    Construct a command to delete a User
    :param user_id: user's id
    :return: Command
    """
    return DeleteUserCommand(user_id)

