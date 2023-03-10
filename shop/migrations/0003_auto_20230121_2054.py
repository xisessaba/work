# Generated by Django 3.2 on 2023-01-21 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20230112_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('phone', models.CharField(max_length=100, verbose_name='Телефон')),
                ('whatsapp', models.CharField(max_length=100, verbose_name='Ватсап')),
                ('message', models.CharField(max_length=100, verbose_name='Сообщение')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.RemoveField(
            model_name='productimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Фото'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='images_2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(необязательно)'),
        ),
        migrations.AddField(
            model_name='product',
            name='images_3',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(необязательно)'),
        ),
        migrations.AddField(
            model_name='product',
            name='images_4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(необязательно)'),
        ),
        migrations.AddField(
            model_name='product',
            name='images_5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото(необязательно)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.brand', verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.productcolor', verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='cpu',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.IntegerField(blank=True, null=True, verbose_name='Оперативная память'),
        ),
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Видеокарта'),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.AddField(
            model_name='applications',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='shop.product', verbose_name='Товар'),
        ),
    ]
