from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание", help_text="Введите описание продукта"
    )

    def __str__(self):
        return f"категория {self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]
        db_table = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(
        null=True, blank=True, verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="Products")
    purchase_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"продукт - {self.name} из категории - {self.category}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        db_table = "Продукты"
