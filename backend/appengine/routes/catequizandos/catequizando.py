# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from google.appengine.ext import blobstore
from catequizando_app.catequizando_model import Catequizando
from config.template_middleware import TemplateResponse
from routes.catequizandos.upload import edit, delete
from tekton import router
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from routes.catequizandos import upload
from gaecookie.decorator import no_csrf
from gaepermission.decorator import permissions
from permission_app.model import CATEQUISTA, ADMIN, COORDENADOR, CATEQUIZANDO


@no_csrf
@permissions(ADMIN, COORDENADOR)
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None

    if key_id:
        context["catechized"] = Catequizando.get_by_id(key_id)
        success_url = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
    else:
        context["catechized"] = Catequizando()
        # gera url para save
        success_url = router.to_path(upload)

    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    context["nav_active"] = 'catequizandos'
    context["upload_url"] = url
    return TemplateResponse(context, template_path='/catequizandos/catequizando.html')

