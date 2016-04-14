from django.conf.urls import url

import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/profile', views.user_profile, name='user_profile'),
    url(r'^accounts/edit', views.user_edit, name='user_edit'),
    url(r'^accounts/settings', views.user_settings, name='user_settings'),
]
