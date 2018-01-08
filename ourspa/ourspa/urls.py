from django.urls import include, re_path

urlpatterns = [
    re_path(r'^api/', include('spauser.urls')),
    re_path(r'^api/', include('otp.urls')),
]
