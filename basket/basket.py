from decimal import Decimal
from django.conf import settings

class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if not basket:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {
                'count': 0,
                'price_per_day': str(product.price_per_day),
                'deposit': str(product.deposit)}
        if update_count:
            self.basket[product_id]['count'] = count
        else:
            self.basket[product_id]['count'] += count
        
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        from shop.models import Equipment
        products = Equipment.objects.filter(id__in=product_ids)
        
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price_per_day'] = Decimal(item['price_per_day'])
            item['deposit'] = Decimal(item['deposit'])
            item['total_price_per_day'] = item['price_per_day'] * item['count']
            item['total_deposit'] = item['deposit'] * item['count']
            yield item

    def __len__(self):
        return sum(item['count'] for item in self.basket.values())

    def get_total_price_per_day(self):
        return sum(Decimal(item['price_per_day']) * item['count'] for item in self.basket.values())

    def get_total_deposit(self):
        return sum(Decimal(item['deposit']) * item['count'] for item in self.basket.values())

    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()