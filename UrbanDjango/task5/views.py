from django.shortcuts import render
from .forms import UserRegister, users
from django.http import HttpResponse,HttpResponseServerError
from django import forms

# Create your views here.









def sign_up_by_html(request):
    info = {'error': [],'number': 1}
    if request.method == "POST":
        is_corect = True
        login = request.POST.get("login")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")
        print(f'''
        login {login}
        password {password}
        repeat_password {repeat_password}
        age {age}
        ''')
        if password != repeat_password:
            is_corect = False
            info['error'].append('Пароли не совпадают.')
        if int(age) < 18:
            is_corect = False
            info['error'].append('Вы должны быть старше 18.')
        for user in users:
            if login == user:
                is_corect = False
                info['error'].append('Пользователь уже существует.')
                break
        if is_corect:
            return HttpResponse(f"Приветствуем, {login}!")
    return render(request,"fifth_task/registration_page.html", {'info':info})


def sign_up_by_django (request):
    info = {'error': [],'number': 2}
    if request.method == "POST":
        is_corect = True
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data["login"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]
        login = request.POST.get("login")
        for user in users:
            if login == user:
                is_corect = False
                info['error'].append('Пользователь уже существует')
        password = hash(request.POST.get("password"))
        repeat_password = hash(request.POST.get("repeat_password"))
        if password != repeat_password:
            is_corect = False
            info['error'].append('Пароли не совпадают')
        age = request.POST.get("age")
        if int(age)<18:
            is_corect = False
            info['error'].append('Вы должны быть старше 18')
        if is_corect:
            return HttpResponse(f"Приветствуем, {login}!")
    else:
        form = UserRegister()
    return render(request,"fifth_task/registration_page.html",{"form":form,'info':info})


