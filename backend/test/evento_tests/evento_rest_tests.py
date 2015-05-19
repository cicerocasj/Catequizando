# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from evento_app.evento_model import Evento
from routes.eventos import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Evento)
        mommy.save_one(Evento)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        evento_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'start', 'end', 'description', 'title']), set(evento_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Evento.query().get())
        json_response = rest.new(None, start='start_string', end='end_string', description='description_string', title='title_string')
        db_evento = Evento.query().get()
        self.assertIsNotNone(db_evento)
        self.assertEquals('start_string', db_evento.start)
        self.assertEquals('end_string', db_evento.end)
        self.assertEquals('description_string', db_evento.description)
        self.assertEquals('title_string', db_evento.title)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['start', 'end', 'description', 'title']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        evento = mommy.save_one(Evento)
        old_properties = evento.to_dict()
        json_response = rest.edit(None, evento.key.id(), start='start_string', end='end_string', description='description_string', title='title_string')
        db_evento = evento.key.get()
        self.assertEquals('start_string', db_evento.start)
        self.assertEquals('end_string', db_evento.end)
        self.assertEquals('description_string', db_evento.description)
        self.assertEquals('title_string', db_evento.title)
        self.assertNotEqual(old_properties, db_evento.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        evento = mommy.save_one(Evento)
        old_properties = evento.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, evento.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['start', 'end', 'description', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, evento.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        evento = mommy.save_one(Evento)
        rest.delete(None, evento.key.id())
        self.assertIsNone(evento.key.get())

    def test_non_evento_deletion(self):
        non_evento = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_evento.key.id())
        self.assertIsNotNone(non_evento.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

