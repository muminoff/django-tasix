# Copyright 2016 django-tasix authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from django.conf import settings
from django.http import HttpResponseForbidden
from tasix.network import is_tasix_member


class TasixMiddleware(object):

    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        allow_tasix = getattr(settings, "ALLOW_TASIX", True)
        if allow_tasix and not is_tasix_member(ip_address):
            return HttpResponseForbidden()
