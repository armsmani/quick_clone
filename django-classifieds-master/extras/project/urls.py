from django.conf.urls.defaults import *

from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # add-on apps.
    (r'^registration/', include('registration.urls')),
    
    url(r'^registration/welcome/$',
                           direct_to_template,
                           {'template': 'registration/registration_complete.html'},
                           name='registration_complete'),

    
    (r'^profiles/', include('profiles.urls'), {'success_url': '/profiles/edit/'}),

    # our views (included from the app)
    (r'', include('classifieds.urls')),
)
