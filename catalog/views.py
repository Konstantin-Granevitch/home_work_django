from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    """функция-контроллер для вывода домашней страницы приложения каталог"""

    if request.method == "GET":
        return render(request, "home.html")


def contacts_view(request):
    """функция-контроллер для вывода страницы с контактами приложения каталог"""

    if request.method == "GET":
        return render(request, "contacts.html")

    if request.method == "POST":
        user_name = request.POST.get("name")
        user_phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        return HttpResponse(f"Запрос успешно выполнен, данные пользователя: {user_name}, {user_phone}, {user_message}")
