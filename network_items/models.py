from django.db import models
from django.utils import timezone


class ContactsData(models.Model):
    email = models.EmailField(verbose_name='Email', max_length=255)
    country = models.CharField(verbose_name='Страна', max_length=255)
    city = models.CharField(verbose_name='Город', max_length=255)
    street = models.CharField(verbose_name='Улица', max_length=255)
    house_number = models.CharField(verbose_name='Номер дома', max_length=255)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.email}, {self.country}, {self.city}'


class Product(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    release_date = models.DateField(verbose_name='Дата выхода', null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class BaseItem(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    contacts_data = models.ForeignKey(ContactsData, verbose_name='Контакты', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Factory(BaseItem):
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(BaseItem):
    provider = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class Entrepreneur(BaseItem):
    provider = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'
