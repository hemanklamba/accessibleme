from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^main/', include('main_app.urls')),
    url(r'^admin/', admin.site.urls),
]