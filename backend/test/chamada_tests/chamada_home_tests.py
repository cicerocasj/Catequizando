# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from chamada_app.chamada_model import Chamada
from routes.chamadas.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Chamada)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        chamada = mommy.save_one(Chamada)
        redirect_response = delete(chamada.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(chamada.key.get())

    def test_non_chamada_deletion(self):
        non_chamada = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_chamada.key.id())
        self.assertIsNotNone(non_chamada.key.get())

