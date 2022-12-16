from django.contrib import admin
from django.urls import path, include, re_path

from django.views.static import serve
from .settings import MEDIA_ROOT

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
