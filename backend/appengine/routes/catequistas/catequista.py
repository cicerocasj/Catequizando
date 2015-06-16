# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.api.app_identity.app_identity import get_default_gcs_bucket_name
from google.appengine.ext import blobstore
from catequista_app.catequista_model import Catequista
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required, permissions
from config.template_middleware import TemplateResponse
from permission_app.model import ALL_PERMISSIONS_LIST
from routes.catequistas import upload
from routes.catequistas.upload import edit, delete
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
        success_url = router.to_path(edit)
        context["delete_path"] = router.to_path(delete)
        context["groups"] = context["catequista"].groups
    else:
        context["catequista"] = Catequista()
        # gera url para save
        success_url = router.to_path(upload)
        context["groups"] = []
    context["choice_groups"] = ALL_PERMISSIONS_LIST
    bucket = get_default_gcs_bucket_name()
    url = blobstore.create_upload_url(success_url, gs_bucket_name=bucket)
    context["upload_url"] = url
    context["nav_active"] = 'catequistas'
    return TemplateResponse(context, template_path='/catequistas/catequista.html')