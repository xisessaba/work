from django.db import models





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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='brands', verbose_name='Категория')
    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"
        


class ProductColor(models.Model):

    name = models.CharField(max_length=100, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', verbose_name='Бренд')
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Цена")
    image = models.ImageField(verbose_name='Фото')
    images_2 = models.ImageField(null=True,blank=True,verbose_name='Фото(необязательно)')
    images_3 = models.ImageField(null=True,blank=True,verbose_name='Фото(необязательно)')
    images_4 = models.ImageField(null=True,blank=True,verbose_name='Фото(необязательно)')
    images_5 = models.ImageField(null=True,blank=True,verbose_name='Фото(необязательно)')
    description = models.TextField(verbose_name="Описание")
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, related_name='products', verbose_name='Цвет')
    cpu = models.CharField(max_length=100, null=True, blank=True, verbose_name="Процессор")
    ram = models.IntegerField(null=True, blank=True,verbose_name="Оперативная память")
    video = models.CharField(max_length=100,null=True, blank=True, verbose_name="Видеокарта")
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




class Applications(models.Model):
    shop = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='applications', verbose_name='Товар')
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    whatsapp = models.CharField(max_length=100, verbose_name="Ватсап")
    message = models.CharField(max_length=100, verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural  = 'Заявки'

    def str(self):
        return self.name




















 



