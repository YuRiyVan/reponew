from django.db import models


class Product(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imgg = models.ForeignKey(
        "Product_img", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.IntegerField()
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product_img(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="shop\static\shop\prod_img")

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

    def __str__(self):
        return self.name
