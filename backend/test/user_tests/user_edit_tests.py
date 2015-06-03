# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from user_app.user_model import User
from routes.users.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        user = mommy.save_one(User)
        template_response = index(user.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        user = mommy.save_one(User)
        old_properties = user.to_dict()
        redirect_response = save(user.key.id(), password='password_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_user = user.key.get()
        self.assertEquals('password_string', edited_user.password)
        self.assertNotEqual(old_properties, edited_user.to_dict())

    def test_error(self):
        user = mommy.save_one(User)
        old_properties = user.to_dict()
        template_response = save(user.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['password']), set(errors.keys()))
        self.assertEqual(old_properties, user.key.get().to_dict())
        self.assert_can_render(template_response)
