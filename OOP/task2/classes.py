class Goods:
    total_count = 0
    total_sum = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Goods.total_count += 1
        Goods.total_sum += price

    @property
    def avg_total(self):
        return round(Goods.total_sum / Goods.total_count)

    def print_info(self):
        print('Этот товар называется', self.name, '. Его цена', self.price)

    def print_avg(self):
        print('Средняя цена всех товаров в корзине - ', self.avg_total)

    def __eq__(self, other):
        return self.price == other.price


class TV(Goods):
    def __init__(self, name, price, diagonal):
        super().__init__(name, price)
        self.diagonal = diagonal

    def print_info(self):
        super().print_info()
        print('Он относится к категории телевизоры')


class Phone(Goods):
    def __init__(self, name, price):
        super().__init__(name, price)

    def call(self):
        print('Динь - Дон, это мелодия телефона', self.name)

