# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from chamada_app.chamada_model import Chamada
from routes.chamadas.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Chamada.query().get())
        redirect_response = save(encontro='encontro_string', data='data_string', catequizandos='catequizandos_string', turma='turma_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_chamada = Chamada.query().get()
        self.assertIsNotNone(saved_chamada)
        self.assertEquals('encontro_string', saved_chamada.encontro)
        self.assertEquals('data_string', saved_chamada.data)
        self.assertEquals('catequizandos_string', saved_chamada.catequizandos)
        self.assertEquals('turma_string', saved_chamada.turma)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['encontro', 'data', 'catequizandos', 'turma']), set(errors.keys()))
        self.assert_can_render(template_response)
