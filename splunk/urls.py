from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_url
urlpatterns = [
    # Examples:
    # url(r'^$', 'splunk.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0,9])', tv.withparam),
    url(r'^teacher', include(teacher_url)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),
    url(r'^youname/$', tv.extremParam, {'name': 'lian'}), #额外传参
    url(r'^yourname/$', tv.revParse, name='askname'), #反向解析
]
