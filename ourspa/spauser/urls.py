from django.conf.urls import re_path
from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views
from spauser import views


urlpatterns = [
    re_path(r'^user/view/$', views.SpaUserView.as_view(), name='user-view'),
    re_path(r'^user/delete/$', views.SpaUserDeleteView.as_view(), name='user-delete'),
    re_path(r'^user/logout/all/$', views.SpaUserLogoutAllView.as_view(), name='user-logout-all'),

    # Views are defined in Djoser, but we're assigning custom paths.
    re_path(r'^user/create/$', djoser_views.UserCreateView.as_view(), name='user-create'),

    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    re_path(r'^user/login/$', jwt_views.ObtainJSONWebToken.as_view(), name='user-login'),
    re_path(r'^user/login/refresh/$', jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
]
