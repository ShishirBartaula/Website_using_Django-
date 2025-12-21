from django.http import HttpResponse
from django.shortcuts import render
#render for templates i.e to show index.html files

#views ---->urls.py

def Home(request):
    return render(request,'myPage/index.html')  # work as request->singel response so one output show
    return HttpResponse("Hello World!!")

def privacy(request):
    return render(request,"mypage/privacy.html")
    

def About(request):  # url ma About request garda tala ko response dine 
    # return HttpResponse("creat view in chiaaurdhango")
    return render(request,'mypage/about.html')

def contact(request):
    # return HttpResponse("contact if you need any help")
    return render(request,'mypage/contact.html')

