from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
urlpatterns = [
    # Examples:
    # url(r'^$', 'splunk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0,9])', tv.withparam),
]
