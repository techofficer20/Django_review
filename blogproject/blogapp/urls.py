from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = "detail"),
    # 사이트 이름/blog/정수 형태로 url을 설계하겠다
    path('new', views.new, name = "new"),
    path('create', views.create, name = "create"),
]