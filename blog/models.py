from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(
        null=True, blank=True, verbose_name="Содержимое", help_text="Введите текст статьи"
    )
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    publication = models.BooleanField(default=False, verbose_name="Признак публикации")
    num_views = models.IntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return f"статья - {self.title}, содержание: {self.content}"

    def count_views(self):
        self.num_views += 1
        self.save()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]
