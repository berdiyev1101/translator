from django.conf.urls.static import static

from .settings import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("translator.urls")),

]

if DEBUG:
    urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
