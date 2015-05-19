# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from evento_app.evento_model import Evento
from routes.eventos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        evento = mommy.save_one(Evento)
        template_response = index(evento.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        evento = mommy.save_one(Evento)
        old_properties = evento.to_dict()
        redirect_response = save(evento.key.id(), start='start_string', end='end_string', description='description_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_evento = evento.key.get()
        self.assertEquals('start_string', edited_evento.start)
        self.assertEquals('end_string', edited_evento.end)
        self.assertEquals('description_string', edited_evento.description)
        self.assertEquals('title_string', edited_evento.title)
        self.assertNotEqual(old_properties, edited_evento.to_dict())

    def test_error(self):
        evento = mommy.save_one(Evento)
        old_properties = evento.to_dict()
        template_response = save(evento.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['start', 'end', 'description', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, evento.key.get().to_dict())
        self.assert_can_render(template_response)
