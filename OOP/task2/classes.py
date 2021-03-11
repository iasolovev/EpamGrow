class Goods:
    total_count = 0
    total_sum = 0

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        Goods.total_count += 1
        Goods.total_sum += price

    @property
    def avg_total(self):
        return round(Goods.total_sum / Goods.total_count)

    def print_info(self):
        return f'Этот товар называется {self.name}. Его цена {self.price}'

    def print_avg(self):
        return f'Средняя цена всех товаров в корзине - {self.avg_total}'

    def __eq__(self, other):
        return self.price == other.price


class TV(Goods):
    def __init__(self, name: str, price: float, diagonal: float):
        super().__init__(name, price)
        self.diagonal = diagonal

    def print_info(self):
        super().print_info()
        return 'Он относится к категории телевизоры'

    def __eq__(self, other):
        return super().__eq__(other) and self.name == other.name and self.diagonal == other.diagonal


class Phone(Goods):
    def __init__(self, name: str, price: float, os: str):
        super().__init__(name, price)
        self.os = os

    def call(self):
        return f'Динь - Дон, это мелодия телефона {self.name}'

    def __eq__(self, other):
        return super().__eq__(other) and self.name == other.name and self.os == other.os
