# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton.gae.middleware.redirect import RedirectResponse
from gaepermission.base_commands import log_main_user_in
from user_app.user_model import User


@login_not_required
@no_csrf
def index(_resp, **data):
    user = User.query(User.password==data.get('password'), User.username==data.get('username'))
    if user.count():
        log_main_user_in(user.fetch()[0], _resp, 'userck')
        return RedirectResponse(data.get('ret_path'))
    context = {
        'username': data.get('username'),
        'error': u'Usuário e/ou senha inválido'
    }
    return TemplateResponse(context, template_path='/login/home.html')