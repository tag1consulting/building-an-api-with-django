from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^totp/create/$', views.TOTPCreateView.as_view(), name='totp-create'),
    re_path(r'^totp/login/(?P<token>[0-9]{6})/$', views.TOTPVerifyView.as_view(), name='totp-login'),
    re_path(r'^totp/delete/$', views.TOTPDeleteView.as_view(), name='totp-delete'),
    re_path(r'^static/create/$', views.StaticCreateView.as_view(), name='static-create'),
    re_path(r'^static/login/(?P<token>[a-z2-9]{7,8})/$', views.StaticVerifyView.as_view(), name='static-login'),
]
