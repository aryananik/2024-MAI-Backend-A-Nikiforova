from django.db import models

class User(models.Model):
    login = models.CharField(max_length=100, verbose_name="Логин")
    password = models.CharField(max_length=256, verbose_name="Пароль")
    age = models.IntegerField(verbose_name="Возраст")
class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название ресторана")
    address = models.CharField(max_length=200, verbose_name="Адрес ресторана")

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена товара")
    is_vegetarian = models.BooleanField(default=False, verbose_name="Вегетарианский товар")

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость заказа")
    delivery_address = models.CharField(max_length=200, verbose_name="Адрес доставки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания заказа")

    def __str__(self):
        return f"Order {self.pk} - Total: {self.total_price}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.item.name} in Order {self.order.pk}"
