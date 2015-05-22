# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from profile_app.profile_model import Profile
from routes.profiles import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Profile)
        mommy.save_one(Profile)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        profile_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'user', 'tipo']), set(profile_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Profile.query().get())
        json_response = rest.new(None, user='user_string', tipo='tipo_string')
        db_profile = Profile.query().get()
        self.assertIsNotNone(db_profile)
        self.assertEquals('user_string', db_profile.user)
        self.assertEquals('tipo_string', db_profile.tipo)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['user', 'tipo']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        profile = mommy.save_one(Profile)
        old_properties = profile.to_dict()
        json_response = rest.edit(None, profile.key.id(), user='user_string', tipo='tipo_string')
        db_profile = profile.key.get()
        self.assertEquals('user_string', db_profile.user)
        self.assertEquals('tipo_string', db_profile.tipo)
        self.assertNotEqual(old_properties, db_profile.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        profile = mommy.save_one(Profile)
        old_properties = profile.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, profile.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['user', 'tipo']), set(errors.keys()))
        self.assertEqual(old_properties, profile.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        profile = mommy.save_one(Profile)
        rest.delete(None, profile.key.id())
        self.assertIsNone(profile.key.get())

    def test_non_profile_deletion(self):
        non_profile = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_profile.key.id())
        self.assertIsNotNone(non_profile.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

