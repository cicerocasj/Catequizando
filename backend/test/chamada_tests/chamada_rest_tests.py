# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from chamada_app.chamada_model import Chamada
from routes.chamadas import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Chamada)
        mommy.save_one(Chamada)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        chamada_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'encontro', 'data', 'catequizandos', 'turma']), set(chamada_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Chamada.query().get())
        json_response = rest.new(None, encontro='encontro_string', data='data_string', catequizandos='catequizandos_string', turma='turma_string')
        db_chamada = Chamada.query().get()
        self.assertIsNotNone(db_chamada)
        self.assertEquals('encontro_string', db_chamada.encontro)
        self.assertEquals('data_string', db_chamada.data)
        self.assertEquals('catequizandos_string', db_chamada.catequizandos)
        self.assertEquals('turma_string', db_chamada.turma)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['encontro', 'data', 'catequizandos', 'turma']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        chamada = mommy.save_one(Chamada)
        old_properties = chamada.to_dict()
        json_response = rest.edit(None, chamada.key.id(), encontro='encontro_string', data='data_string', catequizandos='catequizandos_string', turma='turma_string')
        db_chamada = chamada.key.get()
        self.assertEquals('encontro_string', db_chamada.encontro)
        self.assertEquals('data_string', db_chamada.data)
        self.assertEquals('catequizandos_string', db_chamada.catequizandos)
        self.assertEquals('turma_string', db_chamada.turma)
        self.assertNotEqual(old_properties, db_chamada.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        chamada = mommy.save_one(Chamada)
        old_properties = chamada.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, chamada.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['encontro', 'data', 'catequizandos', 'turma']), set(errors.keys()))
        self.assertEqual(old_properties, chamada.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        chamada = mommy.save_one(Chamada)
        rest.delete(None, chamada.key.id())
        self.assertIsNone(chamada.key.get())

    def test_non_chamada_deletion(self):
        non_chamada = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_chamada.key.id())
        self.assertIsNotNone(non_chamada.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

