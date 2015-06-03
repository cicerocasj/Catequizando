# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from user_app import user_facade
from routes.users import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = user_facade.list_users_cmd()
    users = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    user_form = user_facade.user_form()

    def localize_user(user):
        user_dct = user_form.fill_with_model(user)
        user_dct['edit_path'] = router.to_path(edit_path, user_dct['id'])
        user_dct['delete_path'] = router.to_path(delete_path, user_dct['id'])
        return user_dct

    localized_users = [localize_user(user) for user in users]
    context = {'users': localized_users,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'users/user_home.html')


def delete(user_id):
    user_facade.delete_user_cmd(user_id)()
    return RedirectResponse(router.to_path(index))

