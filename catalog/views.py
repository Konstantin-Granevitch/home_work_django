from django.shortcuts import render


def home_view(request):
    """функция-контроллер для вывода домашней страницы приложения каталог"""

    if request.method == "GET":
        return render(request, 'catalog/home.html')

def contacts_view(request):
    """функция-контроллер для вывода страницы с контактами приложения каталог"""

    if request.method == "GET":
        return render(request, 'catalog/contacts.html')
