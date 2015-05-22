# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from formacao_app import formacao_facade
from routes.formacaos import new, edit
from tekton.gae.middleware.redirect import RedirectResponse


@no_csrf
def index():
    cmd = formacao_facade.list_formacaos_cmd()
    formacaos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    formacao_form = formacao_facade.formacao_form()

    def localize_formacao(formacao):
        formacao_dct = formacao_form.fill_with_model(formacao)
        formacao_dct['edit_path'] = router.to_path(edit_path, formacao_dct['id'])
        formacao_dct['delete_path'] = router.to_path(delete_path, formacao_dct['id'])
        return formacao_dct

    localized_formacaos = [localize_formacao(formacao) for formacao in formacaos]
    context = {'formacaos': localized_formacaos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context, 'formacaos/formacao_home.html')


def delete(formacao_id):
    formacao_facade.delete_formacao_cmd(formacao_id)()
    return RedirectResponse(router.to_path(index))

