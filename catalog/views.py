from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.views import View

from .models import Product


class HomeView(View):
    """контроллер для вывода домашней страницы приложения каталог со списком продуктов"""

    def get(self, request):
        product_list = Product.objects.all()
        context = {'product_list': product_list}
        return render(request, "catalog/home.html", context)


class ContactsView(View):
    """контроллер для вывода страницы с контактами приложения каталог"""

    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        user_name = request.POST.get("name")
        user_phone = request.POST.get("phone")
        user_message = request.POST.get("message")
        return HttpResponse(f"Запрос успешно выполнен, данные пользователя: {user_name}, {user_phone}, {user_message}")


class ProductDetailView(DetailView):
    """контроллер для вызова страницы с описанием товара"""

    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product_list'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return obj
