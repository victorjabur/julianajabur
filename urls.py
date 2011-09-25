from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'julianajaburapp.views.handle_error404'
handler500 = 'julianajaburapp.views.handle_error500'

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'julianajabur.views.home', name='home'),
    # url(r'^julianajabur/', include('julianajabur.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
#)

urlpatterns = patterns('julianajaburapp.views',
    (r'^polls/$', 'index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote')
)

urlpatterns += patterns('',
    (r'^admin/', include(admin.site.urls)),
)