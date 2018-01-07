from django.conf.urls import re_path

from djoser import views as djoser_views
from rest_framework_jwt import views as jwt_views


urlpatterns = [
    # Views are defined in Djoser, but we're assigning custom paths.
    re_path(r'^user/view/$', djoser_views.UserView.as_view(), name='user-view'),
    re_path(r'^user/delete/$', djoser_views.UserDeleteView.as_view(), name='user-delete'),
    re_path(r'^user/create/$', djoser_views.UserCreateView.as_view(), name='user-create'),

    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    re_path(r'^user/login/$', jwt_views.ObtainJSONWebToken.as_view(), name='user-login'),
    re_path(r'^user/login/refresh/$', jwt_views.RefreshJSONWebToken.as_view(), name='user-login-refresh'),
]
