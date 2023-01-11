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
    category_description = models.TextField(blank=True,verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('phone', 'Телефоны'),
        ('laptop', 'Ноутбуки'),
    )



    name = models.CharField(max_length=100, verbose_name="Название")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,verbose_name="Категория" )
    category_model = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Модель")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")
    image = models.ImageField(upload_to='images/', verbose_name="Фото")
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















 



