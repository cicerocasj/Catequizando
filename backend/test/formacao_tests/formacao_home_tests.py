# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from formacao_app.formacao_model import Formacao
from routes.formacaos.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Formacao)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        formacao = mommy.save_one(Formacao)
        redirect_response = delete(formacao.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(formacao.key.get())

    def test_non_formacao_deletion(self):
        non_formacao = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_formacao.key.id())
        self.assertIsNotNone(non_formacao.key.get())

