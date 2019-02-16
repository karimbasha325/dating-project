"""datingapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView),
    url(r'^resort/', views.resortview),
    url(r'^about/', views.aboutview),
    url(r'^service/', views.serviceview),
    url(r'^book/', views.Bookticketview),
    url(r'^success/', views.successview),
    url(r'^signup/', views.signup_view),
    url(r'^logout/', views.logout_view),
    url(r'^bookinglist/', views.Booktickets_list,name='list'),
    url(r'^detail/(?P<pk>\d+)/$', views.UserDetails.as_view(),name='detail'),
    url(r'^ticketdetail/(?P<pk>\d+)/$', views.BookticketsDetail.as_view(),name='ticketdetail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),

]
