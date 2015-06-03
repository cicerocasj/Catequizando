# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from user_app.user_model import User
from routes.users import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(User)
        mommy.save_one(User)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        user_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'password']), set(user_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(User.query().get())
        json_response = rest.new(None, password='password_string')
        db_user = User.query().get()
        self.assertIsNotNone(db_user)
        self.assertEquals('password_string', db_user.password)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['password']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        user = mommy.save_one(User)
        old_properties = user.to_dict()
        json_response = rest.edit(None, user.key.id(), password='password_string')
        db_user = user.key.get()
        self.assertEquals('password_string', db_user.password)
        self.assertNotEqual(old_properties, db_user.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        user = mommy.save_one(User)
        old_properties = user.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, user.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['password']), set(errors.keys()))
        self.assertEqual(old_properties, user.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        user = mommy.save_one(User)
        rest.delete(None, user.key.id())
        self.assertIsNone(user.key.get())

    def test_non_user_deletion(self):
        non_user = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_user.key.id())
        self.assertIsNotNone(non_user.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

