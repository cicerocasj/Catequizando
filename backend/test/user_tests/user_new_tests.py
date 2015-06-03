# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from user_app.user_model import User
from routes.users.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(User.query().get())
        redirect_response = save(password='password_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_user = User.query().get()
        self.assertIsNotNone(saved_user)
        self.assertEquals('password_string', saved_user.password)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['password']), set(errors.keys()))
        self.assert_can_render(template_response)
