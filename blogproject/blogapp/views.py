from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog # models.py에 있는 Blog 객체를 받아와야 함.
# Create your views here.

def home(request):
    blogs = Blog.objects 
    blog_list = Blog.objects.all() # 블로그 모든 글들을 대상으로 
    paginator = Paginator(blog_list, 3) # 블로그 객체 세 개를 한 페이지로 자르기
    page = request.GET.get('page') # request된 페이지가 뭔지를 알아내고
    posts = paginator.get_page(page) # request된 페이지를 얻어온 뒤 return 해 준다.
    # 쿼리셋: Blog.objects와 같은 것들..
    # 메소드: 쿼리셋을 좀 더 유용하게 쓸 수 있도록 해주는 것
    # 쿼리셋과 메소드의 형식
    # 모델.쿼리셋(objects).메소드
    # blogs = Blog.objects
    # blogs.all() = Blog.objects.all()
    return render(request, "home.html", {'blogs' : blogs, 'posts' : posts})

def detail(request, blog_id): # request만으로는 정보 부족. 몇 번 객체를 다룰 것인지 정보 필요.
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    # pk = primary key. 객체들의 이름표, 구분자, 데이터의 대표값
    return render(request, "detail.html", {'details' : blog_detail})

def new(request):
    return render(request, "new.html")

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))