from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
import django.contrib.auth
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
	url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^accounts/login/$', login),
	url(r'^logout/$', logout_page),
]