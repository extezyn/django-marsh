from django.db import models

class Category(models.Model):
        name = models.CharField(max_length=100, verbose_name="Название категории")
        description = models.TextField(verbose_name="Описание")

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = "Категория"
            verbose_name_plural = "Категории"


class Equipment(models.Model):
        name = models.CharField(max_length=100, verbose_name="Название")
        category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
        description = models.TextField(verbose_name="Описание")
        price_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за день")
        deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Залог")
        photo = models.ImageField(upload_to='equipment/', verbose_name="Фото")
        is_available = models.BooleanField(default=True, verbose_name="Доступно")

        def __str__(self):
            return self.name

        class Meta:
            verbose_name = "Инвентарь"
            verbose_name_plural = "Инвентарь"


class Client(models.Model):
        first_name = models.CharField(max_length=50, verbose_name="Имя")
        last_name = models.CharField(max_length=50, verbose_name="Фамилия")
        phone = models.CharField(max_length=20, verbose_name="Телефон")
        email = models.EmailField(verbose_name="Email")
        passport = models.CharField(max_length=20, verbose_name="Паспорт")

        def __str__(self):
            return f"{self.last_name} {self.first_name}"

        class Meta:
            verbose_name = "Клиент"
            verbose_name_plural = "Клиенты"


class Rental(models.Model):
        equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Инвентарь")
        client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
        start_date = models.DateField(verbose_name="Дата начала")
        end_date = models.DateField(verbose_name="Дата окончания")
        total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
        is_active = models.BooleanField(default=True, verbose_name="Активна")

        def __str__(self):
            return f"Аренда #{self.id}"

        class Meta:
            verbose_name = "Аренда"
            verbose_name_plural = "Аренды"


class DamageReport(models.Model):
        rental = models.ForeignKey(Rental, on_delete=models.CASCADE, verbose_name="Аренда")
        description = models.TextField(verbose_name="Описание повреждения")
        photo = models.ImageField(upload_to='damages/', verbose_name="Фото повреждения")
        repair_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость ремонта")
        date_reported = models.DateField(auto_now_add=True, verbose_name="Дата сообщения")

        def __str__(self):
            return f"Повреждение #{self.id}"

        class Meta:
            verbose_name = "Повреждение"
            verbose_name_plural = "Повреждения"


class Payment(models.Model):
        rental = models.ForeignKey(Rental, on_delete=models.CASCADE, verbose_name="Аренда")
        amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
        payment_date = models.DateField(auto_now_add=True, verbose_name="Дата платежа")
        payment_method = models.CharField(max_length=50, choices=[
            ('cash', 'Наличные'),
            ('card', 'Карта'),
            ('transfer', 'Перевод')
        ], verbose_name="Способ оплаты")

        def __str__(self):
            return f"Платеж #{self.id}"

        class Meta:
            verbose_name = "Платеж"
            verbose_name_plural = "Платежи"


class Employee(models.Model):
        first_name = models.CharField(max_length=50, verbose_name="Имя")
        last_name = models.CharField(max_length=50, verbose_name="Фамилия")
        position = models.CharField(max_length=100, verbose_name="Должность")
        hire_date = models.DateField(verbose_name="Дата приема")

        def __str__(self):
            return f"{self.last_name} {self.first_name}"

        class Meta:
            verbose_name = "Сотрудник"
            verbose_name_plural = "Сотрудники"


class Maintenance(models.Model):
        equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name="Инвентарь")
        employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
        maintenance_date = models.DateField(verbose_name="Дата обслуживания")
        description = models.TextField(verbose_name="Описание работ")
        is_completed = models.BooleanField(default=False, verbose_name="Завершено")

        def __str__(self):
            return f"Обслуживание #{self.id}"

        class Meta:
            verbose_name = "Обслуживание"
            verbose_name_plural = "Обслуживание"
            
class Order(models.Model):
     SHOP = "SH"
     COURIER = "CR"
     PICKUPPOINT = "PP"
     TYPE_DELIVERY = [
          (SHOP, "Вывоз из магазина"),
          (COURIER, "Доставка курьером"),
          (PICKUPPOINT, "Пункт выдачт заказов"),
     ]

     buyer_firstname = models.CharField(max_length=50, verbose_name="Фамилия покупателя")
     buyer_name = models.CharField(max_length=50, verbose_name="Имя покупателя")
     buyer_surname = models.CharField(max_length=50, verbose_name="Отчество покупателя")
     comment = models.TextField(max_length=200, blank= True, null=True, verbose_name="комментарий к заказу")
     delivery_address = models.CharField(max_length=100, verbose_name="адрес доставки")
     delivery_type = models.CharField(max_length=2,choices=TYPE_DELIVERY,default=SHOP ,verbose_name="способо доставки")
     daet_create = models.DateTimeField(auto_now_add=True, verbose_name="дата создания заказа")
     date_finish = models.DateTimeField(blank=True, null=True, verbose_name="дата завершения заказа")

     equipment = models.ManyToManyField('Equipment', through='Pos_order', verbose_name='Товар')

     def __str__(self):
          return f'#{self.pk} - {self.buyer_firstname} {self.buyer_name ({self.daet_create})}'
     
     class Meta:
          verbose_name = 'Заказ'
          verbose_name_plural = 'Заказы'

class Pos_order(models.Model):
          equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT, verbose_name='Снаряжение')
          order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ') 
          count = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
          discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')

          def __str__(self):
               return f'{self.order.pk} {self.clothes.name} ({self.order.buyer_firstname} {self.order.buyer_name})'
          
          class Meta:
               verbose_name = 'Позиция заказа'
               verbose_name_plural = 'Позиции заказа'
