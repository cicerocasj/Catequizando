# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from chamada_app.chamada_model import Chamada
from routes.chamadas.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        chamada = mommy.save_one(Chamada)
        template_response = index(chamada.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        chamada = mommy.save_one(Chamada)
        old_properties = chamada.to_dict()
        redirect_response = save(chamada.key.id(), encontro='encontro_string', data='data_string', catequizandos='catequizandos_string', turma='turma_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_chamada = chamada.key.get()
        self.assertEquals('encontro_string', edited_chamada.encontro)
        self.assertEquals('data_string', edited_chamada.data)
        self.assertEquals('catequizandos_string', edited_chamada.catequizandos)
        self.assertEquals('turma_string', edited_chamada.turma)
        self.assertNotEqual(old_properties, edited_chamada.to_dict())

    def test_error(self):
        chamada = mommy.save_one(Chamada)
        old_properties = chamada.to_dict()
        template_response = save(chamada.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['encontro', 'data', 'catequizandos', 'turma']), set(errors.keys()))
        self.assertEqual(old_properties, chamada.key.get().to_dict())
        self.assert_can_render(template_response)
