"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),        # URL과 함수를 매핑한것
    path('pybo/', include('pybo.urls')),        # inlucde(A) : pybo/로 시작되는 페이지 요청은 모두 A파일에 있는 URL
    path('common/', include('common.urls')),    # 매핑을 참고라하는 의미
    path('', base_views.index, name='index')
]
