# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from formacao_app.formacao_model import Formacao
from routes.formacoes.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Formacao.query().get())
        redirect_response = save(titulo='titulo_string', data='data_string', conteudo='conteudo_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_formacao = Formacao.query().get()
        self.assertIsNotNone(saved_formacao)
        self.assertEquals('titulo_string', saved_formacao.titulo)
        self.assertEquals('data_string', saved_formacao.data)
        self.assertEquals('conteudo_string', saved_formacao.conteudo)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'data', 'conteudo']), set(errors.keys()))
        self.assert_can_render(template_response)
