from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def home_view(request):
    """функция-контроллер для вывода домашней страницы приложения каталог"""

    product_list = Product.objects.all()
    context = {'product_list': product_list}

    if request.method == "GET":
        return render(request, "catalog/home.html", context)


def contacts_view(request):
    """функция-контроллер для вывода страницы с контактами приложения каталог"""

    if request.method == "GET":
        return render(request, "catalog/contacts.html")

    if request.method == "POST":
        user_name = request.POST.get("name")
        user_phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        return HttpResponse(f"Запрос успешно выполнен, данные пользователя: {user_name}, {user_phone}, {user_message}")


def product_detail(request, pk):
    """контроллер для вызова страницы с описанием товара"""

    product = Product.objects.get(id=pk)
    context = {'product': product}

    return render(request, 'catalog/product_detail.html', context)
