# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from user_app.user_model import User
from routes.users.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(User)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        user = mommy.save_one(User)
        redirect_response = delete(user.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(user.key.get())

    def test_non_user_deletion(self):
        non_user = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_user.key.id())
        self.assertIsNotNone(non_user.key.get())

