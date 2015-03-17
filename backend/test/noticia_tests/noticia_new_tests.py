# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from noticia_app.noticia_model import Noticia
from routes.noticias.new import index, save
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        template_response = index()
        self.assert_can_render(template_response)


class SaveTests(GAETestCase):
    def test_success(self):
        self.assertIsNone(Noticia.query().get())
        redirect_response = save(content='content_string', link='link_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        saved_noticia = Noticia.query().get()
        self.assertIsNotNone(saved_noticia)
        self.assertEquals('content_string', saved_noticia.content)
        self.assertEquals('link_string', saved_noticia.link)
        self.assertEquals('title_string', saved_noticia.title)

    def test_error(self):
        template_response = save()
        errors = template_response.context['errors']
        self.assertSetEqual(set(['content', 'link', 'title']), set(errors.keys()))
        self.assert_can_render(template_response)
