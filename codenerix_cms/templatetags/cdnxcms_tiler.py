# -*- coding: utf-8 -*-
#
# django-codenerix-cms
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django import template

from codenerix_cms.templatetags_tiler import cdnx_tiler, cdnx_tiler_type


def fbuilder2(f):
    return lambda arg1, arg2: f(arg1, arg2)


def fbuilderN(f):
    return lambda *args, **kwargs: f(*args, **kwargs)


register = template.Library()

register.simple_tag(fbuilder2(cdnx_tiler), takes_context=True, name='cdnx_tiler')
register.simple_tag(fbuilderN(cdnx_tiler_type), name='cdnx_tiler_type')
