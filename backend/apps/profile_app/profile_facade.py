# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from profile_app.profile_commands import ListProfileCommand, SaveProfileCommand, UpdateProfileCommand, ProfileForm,\
    GetProfileCommand, DeleteProfileCommand


def save_profile_cmd(**profile_properties):
    """
    Command to save Profile entity
    :param profile_properties: a dict of properties to save on model
    :return: a Command that save Profile, validating and localizing properties received as strings
    """
    return SaveProfileCommand(**profile_properties)


def update_profile_cmd(profile_id, **profile_properties):
    """
    Command to update Profile entity with id equals 'profile_id'
    :param profile_properties: a dict of properties to update model
    :return: a Command that update Profile, validating and localizing properties received as strings
    """
    return UpdateProfileCommand(profile_id, **profile_properties)


def list_profiles_cmd():
    """
    Command to list Profile entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListProfileCommand()


def profile_form(**kwargs):
    """
    Function to get Profile's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return ProfileForm(**kwargs)


def get_profile_cmd(profile_id):
    """
    Find profile by her id
    :param profile_id: the profile id
    :return: Command
    """
    return GetProfileCommand(profile_id)



def delete_profile_cmd(profile_id):
    """
    Construct a command to delete a Profile
    :param profile_id: profile's id
    :return: Command
    """
    return DeleteProfileCommand(profile_id)

