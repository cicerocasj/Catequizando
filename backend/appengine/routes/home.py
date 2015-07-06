# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO


@no_csrf
@permissions(CATEQUISTA)
def index():
    context = {}
    messages = [{
        u'type': u'notice',
        u'date': u'há 40 minutos atrás',
        u'title': u'Papa fala sobre os jovens',
        u'content': u'Em encontro com os jovens de roma, Lorem ipsum dolor sit amet, consectetur adipisicing elit. u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'event',
        u'date': u'há 55 minutos atrás',
        u'title': u'Formação de catequista',
        u'content': u'Dia tal tera uma formação para todos os catequistas da paróquia, dolor sit amet, consectetur adipi u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'notice',
        u'date': u'há 2 horas atrás',
        u'title': u'Papa fala sobre os jovens',
        u'content': u'Em encontro com os jovens de roma, Lorem ipsum dolor sit amet, consectetur adipisicing elit. u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'event',
        u'date': u'há 1 dia atrás',
        u'title': u'Formação de catequista',
        u'content': u'Dia tal tera uma formação para todos os catequistas da paróquia, dolor sit amet, consectetur adipi u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'notice',
        u'date': u'há 40 minutos atrás',
        u'title': u'Papa fala sobre os jovens',
        u'content': u'Em encontro com os jovens de roma, Lorem ipsum dolor sit amet, consectetur adipisicing elit. u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'event',
        u'date': u'há 55 minutos atrás',
        u'title': u'Formação de catequista',
        u'content': u'Dia tal tera uma formação para todos os catequistas da paróquia, dolor sit amet, consectetur adipi u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'notice',
        u'date': u'há 40 minutos atrás',
        u'title': u'Papa fala sobre os jovens',
        u'content': u'Em encontro com os jovens de roma, Lorem ipsum dolor sit amet, consectetur adipisicing elit. u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'notice',
        u'date': u'há 40 minutos atrás',
        u'title': u'Papa fala sobre os jovens',
        u'content': u'Em encontro com os jovens de roma, Lorem ipsum dolor sit amet, consectetur adipisicing elit. u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }, {
        u'type': u'event',
        u'date': u'há 55 minutos atrás',
        u'title': u'Formação de catequista',
        u'content': u'Dia tal tera uma formação para todos os catequistas da paróquia, dolor sit amet, consectetur adipi u'
                   u'Libero laboriosam dolor perspiciatis omnis exercitationem. Beatae, officia pariatur? Est cum u'
                   u'veniam excepturi. Maiores praesentium, porro voluptas suscipit facere rem dicta, debitis.'
    }]
    context["messages"] = messages
    context["nav_active"] = 'início'
    return TemplateResponse(context)

