
from django.contrib import admin
from django.urls import path, include

from apps.home import urls as home_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)), #teste 09.11
    path('home/', include(home_urls)), 
    path('sobre/', include(home_urls)),
    path('penal/', include(home_urls)),
    path('civil/', include(home_urls)),
    path('militar/', include(home_urls)),
    path('bombeiros/', include(home_urls)),
    path('guarda/', include(home_urls)),
]
