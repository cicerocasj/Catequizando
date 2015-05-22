# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from formacao_app.formacao_model import Formacao
from routes.formacaos.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        formacao = mommy.save_one(Formacao)
        template_response = index(formacao.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        formacao = mommy.save_one(Formacao)
        old_properties = formacao.to_dict()
        redirect_response = save(formacao.key.id(), titulo='titulo_string', data='data_string', conteudo='conteudo_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_formacao = formacao.key.get()
        self.assertEquals('titulo_string', edited_formacao.titulo)
        self.assertEquals('data_string', edited_formacao.data)
        self.assertEquals('conteudo_string', edited_formacao.conteudo)
        self.assertNotEqual(old_properties, edited_formacao.to_dict())

    def test_error(self):
        formacao = mommy.save_one(Formacao)
        old_properties = formacao.to_dict()
        template_response = save(formacao.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['titulo', 'data', 'conteudo']), set(errors.keys()))
        self.assertEqual(old_properties, formacao.key.get().to_dict())
        self.assert_can_render(template_response)
