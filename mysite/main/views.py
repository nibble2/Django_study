from django.shortcuts import render

def index(request): # url 입력
    return render(request, 'main/index.html')


def cafelist(request):
    return render(request, 'main/cafelist.html')
