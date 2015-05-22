# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from profile_app.profile_model import Profile



class ProfileSaveForm(ModelForm):
    """
    Form used to save and update Profile
    """
    _model_class = Profile
    _include = [Profile.user, 
                Profile.tipo]


class ProfileForm(ModelForm):
    """
    Form used to expose Profile's properties for list or json
    """
    _model_class = Profile


class GetProfileCommand(NodeSearch):
    _model_class = Profile


class DeleteProfileCommand(DeleteNode):
    _model_class = Profile


class SaveProfileCommand(SaveCommand):
    _model_form_class = ProfileSaveForm


class UpdateProfileCommand(UpdateNode):
    _model_form_class = ProfileSaveForm


class ListProfileCommand(ModelSearchCommand):
    def __init__(self):
        super(ListProfileCommand, self).__init__(Profile.query_by_creation())

