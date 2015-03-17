# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from base import GAETestCase
from datetime import datetime, date
from decimal import Decimal
from noticia_app.noticia_model import Noticia
from routes.noticias.edit import index, save
from mommygae import mommy
from tekton.gae.middleware.redirect import RedirectResponse


class IndexTests(GAETestCase):
    def test_success(self):
        noticia = mommy.save_one(Noticia)
        template_response = index(noticia.key.id())
        self.assert_can_render(template_response)


class EditTests(GAETestCase):
    def test_success(self):
        noticia = mommy.save_one(Noticia)
        old_properties = noticia.to_dict()
        redirect_response = save(noticia.key.id(), content='content_string', link='link_string', title='title_string')
        self.assertIsInstance(redirect_response, RedirectResponse)
        edited_noticia = noticia.key.get()
        self.assertEquals('content_string', edited_noticia.content)
        self.assertEquals('link_string', edited_noticia.link)
        self.assertEquals('title_string', edited_noticia.title)
        self.assertNotEqual(old_properties, edited_noticia.to_dict())

    def test_error(self):
        noticia = mommy.save_one(Noticia)
        old_properties = noticia.to_dict()
        template_response = save(noticia.key.id())
        errors = template_response.context['errors']
        self.assertSetEqual(set(['content', 'link', 'title']), set(errors.keys()))
        self.assertEqual(old_properties, noticia.key.get().to_dict())
        self.assert_can_render(template_response)
