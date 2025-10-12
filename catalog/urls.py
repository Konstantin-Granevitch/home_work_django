from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    path("home/", views.home_view, name="home"),
    path("contacts/", views.contacts_view, name="contacts"),
    path('product/<int:pk>/', views.product_detail, name='product_detail')
]
