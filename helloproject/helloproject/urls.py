"""helloproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import helloapp.views # 새로 추가한 app의 views.py를 import 시키기
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', helloapp.views.home, name = "home"), 
    # 기본적인 index.html 창 연결 방법
    # url이 ''이면, helloapp에 있는 views.py의 home 함수를 호출하라.
    # 그리고 이 url을 이름을 home이라 하겠다.
]

