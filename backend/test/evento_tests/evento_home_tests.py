# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from evento_app.evento_model import Evento
from routes.eventos.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Evento)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        evento = mommy.save_one(Evento)
        redirect_response = delete(evento.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(evento.key.get())

    def test_non_evento_deletion(self):
        non_evento = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_evento.key.id())
        self.assertIsNotNone(non_evento.key.get())

