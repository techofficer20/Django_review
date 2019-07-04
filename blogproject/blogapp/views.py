from django.shortcuts import render
from .models import Blog # models.py에 있는 Blog 객체를 받아와야 함.
# Create your views here.

def home(request):
    blogs = Blog.objects 
    # 쿼리셋: Blog.objects와 같은 것들..
    # 메소드: 쿼리셋을 좀 더 유용하게 쓸 수 있도록 해주는 것
    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
    # blogs = Blog.objects
    # blogs.all() = Blog.objects.all()
    return render(request, "home.html", {'blogs' : blogs})
