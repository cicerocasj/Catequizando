# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from time import sleep
from catequista_app import catequista_facade
from catequista_app.catequista_commands import CatequistaSaveForm
from catequista_app.catequista_model import Catequista
from gaebusiness.business import CommandExecutionException
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from routes import catequistas
from routes.catequistas import download
from tekton import router
from tekton.router import to_path
from tekton.gae.middleware.redirect import RedirectResponse
from google.appengine.ext import blobstore
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from user_app.user_model import User


@login_not_required
@no_csrf
def index(_handler, **catequistas_properties):
    if catequistas_properties.get('files'):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequistas_properties['avatar'] = avatar
        catequistas_properties.pop("files", None)
    if not isinstance(catequistas_properties.get('groups'), list):
        catequistas_properties['groups'] = [catequistas_properties.get('groups')]
    # cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
    user_not_unique = False
    try:
        if catequistas_properties.get('username') and User.is_unique(catequistas_properties.get('username')):
            cmd = Catequista(**catequistas_properties)
            cmd.put()
        else:
            cmd = catequista_facade.save_catequista_cmd(**catequistas_properties)
            user_not_unique = True
    except CommandExecutionException:
        context = {
            'errors': {}
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    if user_not_unique:
        cmd.errors['username'] = unicode(u'Usuário já existe.')
        context = {
            'errors': cmd.errors
        }
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@login_not_required
@no_csrf
def edit(_handler, **catequistas_properties):
    if catequistas_properties.get('files'):
        blob_infos = _handler.get_uploads("files[]")
        blob_key = blob_infos[0].key()
        avatar = to_path(download, blob_key)
        catequistas_properties['avatar'] = avatar
        catequistas_properties.pop("files", None)
    obj_id = catequistas_properties.pop("key_id", None)
    if not isinstance(catequistas_properties.get('groups'), list):
        catequistas_properties['groups'] = [catequistas_properties.get('groups')]
    # cmd = catequista_facade.update_catequista_cmd(obj_id, **catequistas_properties)
    try:
        cmd = Catequista(**catequistas_properties)
        cmd.put()
    except CommandExecutionException:
        success_url = router.to_path(edit)
        bucket = get_default_gcs_bucket_name()
        url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
        context = {'errors': {},
                   'upload_url': url,
                   'catequista': catequistas_properties}
        return TemplateResponse(context, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))


@login_not_required
@no_csrf
def delete(obj_id=0):
    cmd = catequista_facade.delete_catequista_cmd(obj_id)
    try:
        cmd()
    except CommandExecutionException:
        return TemplateResponse({}, template_path='/catequistas/catequista.html')
    sleep(0.5)
    return RedirectResponse(router.to_path(catequistas))