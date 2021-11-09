
from django.contrib import admin
from django.urls import path, include

from apps.home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include(home_urls)), #teste 09.11
    path ('home/', include(home_urls)), 
]
