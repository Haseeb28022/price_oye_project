from django.urls import re_path, include, path
from accounts.views import activation, login_view, success, fail

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.social.urls')),
    # path('api-auth/', include('rest_framework.urls'))
    path('activate/<str:uid>/<str:token>/', activation, name='activation'),
    path('activateRequest/<str:uid>/<str:token>/', login_view,
         name='activateRequest'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
]
