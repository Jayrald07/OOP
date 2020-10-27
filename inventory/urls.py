from django.conf.urls import url
from .views import index, displayLaptops, displayDesktop, displayMobile

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^displayLaptops$',displayLaptops,name='displayLaptops'),
    url(r'^displayDesktops$',displayDesktop,name='displayDesktop'),
    url(r'^displayMobile$',displayMobile,name='displayMobile'),
]