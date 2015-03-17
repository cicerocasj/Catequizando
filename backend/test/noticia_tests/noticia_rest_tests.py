# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from datetime import datetime, date
from decimal import Decimal
from base import GAETestCase
from noticia_app.noticia_model import Noticia
from routes.noticias import rest
from gaegraph.model import Node
from mock import Mock
from mommygae import mommy


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Noticia)
        mommy.save_one(Noticia)
        json_response = rest.index()
        context = json_response.context
        self.assertEqual(2, len(context))
        noticia_dct = context[0]
        self.assertSetEqual(set(['id', 'creation', 'content', 'link', 'title']), set(noticia_dct.iterkeys()))
        self.assert_can_serialize_as_json(json_response)


class NewTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Noticia.query().get())
        json_response = rest.new(None, content='content_string', link='link_string', title='title_string')
        db_noticia = Noticia.query().get()
        self.assertIsNotNone(db_noticia)
        self.assertEquals('content_string', db_noticia.content)
        self.assertEquals('link_string', db_noticia.link)
        self.assertEquals('title_string', db_noticia.title)
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        resp = Mock()
        json_response = rest.new(resp)
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['content', 'link', 'title']), set(errors.keys()))
        self.assert_can_serialize_as_json(json_response)


class EditTests(GAETestCase):
    def test_success(self):
        noticia = mommy.save_one(Noticia)
        old_properties = noticia.to_dict()
        json_response = rest.edit(None, noticia.key.id(), content='content_string', link='link_string', title='title_string')
        db_noticia = noticia.key.get()
        self.assertEquals('content_string', db_noticia.content)
        self.assertEquals('link_string', db_noticia.link)
        self.assertEquals('title_string', db_noticia.title)
        self.assertNotEqual(old_properties, db_noticia.to_dict())
        self.assert_can_serialize_as_json(json_response)

    def test_error(self):
        noticia = mommy.save_one(Noticia)
        old_properties = noticia.to_dict()
        resp = Mock()
        json_response = rest.edit(resp, noticia.key.id())
        errors = json_response.context
        self.assertEqual(500, resp.status_code)
        self.assertSetEqual(set(['content', 'link', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, noticia.key.get().to_dict())
        self.assert_can_serialize_as_json(json_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        noticia = mommy.save_one(Noticia)
        rest.delete(None, noticia.key.id())
        self.assertIsNone(noticia.key.get())

    def test_non_noticia_deletion(self):
        non_noticia = mommy.save_one(Node)
        response = Mock()
        json_response = rest.delete(response, non_noticia.key.id())
        self.assertIsNotNone(non_noticia.key.get())
        self.assertEqual(500, response.status_code)
        self.assert_can_serialize_as_json(json_response)

