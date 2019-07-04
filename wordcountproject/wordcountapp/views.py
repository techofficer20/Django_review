from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def result(request):
    text = request.GET['fulltext'] # textarea name을 fulltext로 정했다.
    words = text.split() # 공백을 기준으로 나눈다.
    word_dictionary = {} # 빈 딕셔너리
    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    return render(request, "result.html", {"full" : text, 'total' : len(words), 'dictionary' : word_dictionary.items()})