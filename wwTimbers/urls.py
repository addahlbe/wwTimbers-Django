from django.conf.urls import (
    patterns,
    include,
    url
)
from django.contrib import admin
from wwTimbers.views import (
    home,
    # contact,
    history,
    decking,
    timbers,
    outdoor,
    crane,
    repair,
)
admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$', home),
    url(r'^history/$', history),
    url(r'^decking/$', decking),
    url(r'^timbers/$', timbers),
    url(r'^outdoor/$', outdoor),
    url(r'^crane/$', crane),
    url(r'^repair/$', repair),
    # url(r'^contact/$', contact),
    url(r'^admin/', include(admin.site.urls)),
)
