"""zqxt_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from calc import views as calc_views

urlpatterns = [
	path('index/',calc_views.index, name='home'),
	path('add/',calc_views.add, name='add'),
    path('add2/<int:a>/<int:b>/', calc_views.old_add2_redirect),

    path('new_add2/<int:a>/<int:b>/', calc_views.add2, name='add2'),
    path('admin/', admin.site.urls),
]
