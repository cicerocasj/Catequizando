# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from noticia_app.noticia_model import Noticia
from routes.noticias.home import index, delete
from gaebusiness.business import CommandExecutionException
from gaegraph.model import Node
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        mommy.save_one(Noticia)
        template_response = index()
        self.assert_can_render(template_response)


class DeleteTests(GAETestCase):
    def test_success(self):
        noticia = mommy.save_one(Noticia)
        redirect_response = delete(noticia.key.id())
        self.assertIsInstance(redirect_response, RedirectResponse)
        self.assertIsNone(noticia.key.get())

    def test_non_noticia_deletion(self):
        non_noticia = mommy.save_one(Node)
        self.assertRaises(CommandExecutionException, delete, non_noticia.key.id())
        self.assertIsNotNone(non_noticia.key.get())

