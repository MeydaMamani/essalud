"""
URL configuration for essalud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('apps.dashboard.urls', namespace='dashboard')),
    path('follow_up/',include('apps.follow_up.urls', namespace='follow_up')),
    path('packages/',include('apps.packages.urls', namespace='packages')),
    path('boards/',include('apps.boards.urls', namespace='boards')),
    path('person/',include('apps.person.urls', namespace='person')),
]
