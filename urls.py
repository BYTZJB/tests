from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin

from core.views.export_view import ExportView

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^export/', ExportView.as_view())
]

urlpatterns += staticfiles_urlpatterns()
