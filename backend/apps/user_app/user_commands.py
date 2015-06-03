# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, NodeSearch, DeleteNode
from user_app.user_model import User



class UserSaveForm(ModelForm):
    """
    Form used to save and update User
    """
    _model_class = User
    _include = [User.password]


class UserForm(ModelForm):
    """
    Form used to expose User's properties for list or json
    """
    _model_class = User


class GetUserCommand(NodeSearch):
    _model_class = User


class DeleteUserCommand(DeleteNode):
    _model_class = User


class SaveUserCommand(SaveCommand):
    _model_form_class = UserSaveForm


class UpdateUserCommand(UpdateNode):
    _model_form_class = UserSaveForm


class ListUserCommand(ModelSearchCommand):
    def __init__(self):
        super(ListUserCommand, self).__init__(User.query_by_creation())

