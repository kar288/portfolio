from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', {'template_name':'sign-in.html'}, name='login'),
    url(r'^login', 'django.contrib.auth.views.login', {'template_name':'sign-in.html'}, name='login'),
    url(r'^sign-in.html', 'django.contrib.auth.views.login', {'template_name':'sign-in.html'}, name='login'),
    
    url(r'^profile$', 'grumblr.views.profile', name='profile'),
    url(r'^registration$', 'grumblr.views.registration', name='registration'),
    url(r'^lost-password.html$', 'grumblr.views.lostpassword'),
    url(r'^recover-password$', 'grumblr.views.recoverpassword', name='recover-password'),
    url(r'^stream$', 'grumblr.views.stream', name = 'stream'),
    url(r'^profile/(?P<name>\w+)', 'grumblr.views.other_user', name = 'other_user'),
    url(r'^edit-information$', 'grumblr.views.edit_information', name ='edit_information'),
    url(r'^search', 'grumblr.views.search', name = 'search'),
    url(r'^logout', 'grumblr.views.logout', name = 'logout'),
    url(r'^edit-password', 'grumblr.views.edit_password', name = 'edit_password'),
    url(r'^dislike', 'grumblr.views.dislike', name = 'dislike'),
    url(r'^disdislike', 'grumblr.views.disdislike', name = 'disdislike'),
    url(r'^photo/(?P<id>\d+)$', 'grumblr.views.get_photo', name='photo'),
    # The following URL should match any username valid in Django and
    # any token produced by the default_token_generator
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'grumblr.views.confirm_registration', name='confirm'),
    url(r'^needs-confirmation.html$', 'grumblr.views.needs_confirmation'), 
    url(r'^grumbls_json.html$', 'grumblr.views.grumbls_json', name="grumbls_json"), 
    

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
