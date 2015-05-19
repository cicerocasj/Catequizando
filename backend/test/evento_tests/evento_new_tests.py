# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from evento_app.evento_model import Evento
from routes.eventos.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Evento.query().get())
        redirect_response = save(start='start_string', end='end_string', description='description_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_evento = Evento.query().get()
        self.assertIsNotNone(saved_evento)
        self.assertEquals('start_string', saved_evento.start)
        self.assertEquals('end_string', saved_evento.end)
        self.assertEquals('description_string', saved_evento.description)
        self.assertEquals('title_string', saved_evento.title)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['start', 'end', 'description', 'title']), set(errors.keys()))
        self.assert_can_render(template_response)
