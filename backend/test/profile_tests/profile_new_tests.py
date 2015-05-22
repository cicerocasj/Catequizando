# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from profile_app.profile_model import Profile
from routes.profiles.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Profile.query().get())
        redirect_response = save(user='user_string', tipo='tipo_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_profile = Profile.query().get()
        self.assertIsNotNone(saved_profile)
        self.assertEquals('user_string', saved_profile.user)
        self.assertEquals('tipo_string', saved_profile.tipo)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['user', 'tipo']), set(errors.keys()))
        self.assert_can_render(template_response)
