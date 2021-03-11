from OOP.task2.classes import *


if __name__ == '__main__':
    tv_1 = TV('LG', 60000, 45)
    tv_2 = TV('Samsung', 80000, 55)

    print(tv_2.print_info())
    print(tv_2.print_avg())

    phone_1 = Phone('Honor', 20000, 'ios')
    phone_2 = Phone('Iphone', 100000, 'ios')

    print(phone_2.print_avg())

    print('Телефоны одинаковые (по цене) -', phone_1 == phone_2)
