# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import




from django.urls import path
from tests.views import TestView

urlpatterns = [
    path('test/', TestView.as_view(), name="test-view"),
]
