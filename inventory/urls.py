from django.conf.urls import url
from .views import index, displayLaptops, displayDesktop, displayMobile, add_laptop, add_desktop, add_mobile

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^displayLaptops$',displayLaptops,name='displayLaptops'),
    url(r'^displayDesktops$',displayDesktop,name='displayDesktop'),
    url(r'^displayMobile$',displayMobile,name='displayMobile'),
    url(r'^addLaptop$',add_laptop,name='add_laptop'),
    url(r'^addDesktop$',add_desktop,name='add_desktop'),
    url(r'^addMobile$',add_mobile,name='add_mobile')

]