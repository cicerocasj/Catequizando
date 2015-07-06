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


