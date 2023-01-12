from django.db import models



class Users(models.Model):
    user = models.CharField(max_length=100, verbose_name="Пользователь")
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True)
    email = models.EmailField(verbose_name="Почта")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")
    # images = models.ManyToManyField(ProductImage, related_name='product')
    description = models.TextField(verbose_name="Описание")
    cpu = models.CharField(max_length=100, verbose_name="Процессор")
    ram = models.IntegerField(verbose_name="Оперативная память")
    video = models.CharField(max_length=100, verbose_name="Видеокарта")
    lte_exists = models.BooleanField(default=True,verbose_name="В наличии")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    def snippet(self):
        return self.description[:50] + '...'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
 
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
 
    def save(self, *args, **kwargs):
        self.image.upload_to = 'product_images/'
        super().save(*args, **kwargs)

class Sale(models.Model):
    shop = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural  = 'Акции'


    def str(self):
        return self.name

    
















 



