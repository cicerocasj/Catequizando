# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from google.appengine.ext import blobstore
from catequista_app.catequista_model import Catequista
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from routes.catequistas import upload
from tekton import router


@login_not_required
@no_csrf
def index(id=0):
    context = {}
    try:
        key_id = int(id)
    except Exception as e:
        key_id = None
    if key_id:
        context["catequista"] = Catequista.get_by_id(key_id)

    # gera url para save
    success_url = router.to_path(upload)
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    context["nav_active"] = 'catequistas'
    context["upload_url"] = url
    return TemplateResponse(context, template_path='/catequistas/catequista.html')