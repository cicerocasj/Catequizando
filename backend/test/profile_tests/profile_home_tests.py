# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from profile_app.profile_model import Profile
from routes.profiles.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Profile)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        profile = mommy.save_one(Profile)
        redirect_response = delete(profile.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(profile.key.get())

    def test_non_profile_deletion(self):
        non_profile = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_profile.key.id())
        self.assertIsNotNone(non_profile.key.get())

