from django.conf.urls import patterns, include, url

from django.contrib import admin
import manuelaWebsite.views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', manuelaWebsite.views.index, name='index'),
    url(r'^recipes/$', manuelaWebsite.views.recipes, name='recipes'),
    url(r'^shop/$', manuelaWebsite.views.shop, name='shop'),
    url(r'^offers/$', manuelaWebsite.views.offers, name='offers'),
    url(r'^contact/$', manuelaWebsite.views.contact, name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
