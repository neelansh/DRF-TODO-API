"""todo URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from app import views

router = routers.SimpleRouter() 

router.register(r'task', views.TaskViewSet, base_name = 'task')


urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^', include('django.contrib.auth.urls')),
    # url(r'^register/$', views.CreateUserView.as_view(), name='user'),
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    # url(r'^accounts/', include('allauth.urls')),
]