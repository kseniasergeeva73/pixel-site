from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='Категория', verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, default='Категория', verbose_name='Название')
    description = models.TextField(default='', verbose_name='Описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    img = models.ImageField(upload_to='media/', default=None, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class ShoppingCart(models.Model):
    id = models.AutoField(primary_key=True)
    products = models.ManyToManyField(Product, verbose_name='Товары', default=None)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self) -> str:
        return self.user.email

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        ShoppingCart.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.shoppingcart.save()
    
