import os
import csv
import analyzer
from datetime import date
from random import randint
from dotenv import load_dotenv

load_dotenv('../outputs/.env.example')

orders = os.getenv('ORDERS')
output_dir = os.getenv('OUTPUT_DIR')

def main():
    orders_list = []

    with open(f'../{orders}', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for read in reader:
            if read[0] == 'order_id':
                continue

            try:
                orders_list.append(
                    {
                        'order_id': int(read[0]), 'product': read[1],
                        'price': float(read[2]), 'quantity': int(read[3]),
                        'total': analyzer.calculate_total(read[2], read[3])
                    }
                )
            except ValueError as e:
                print(f'Ошибка преобразования -> {e}')

    total_orders = analyzer.calculate_orders_total(orders_list)
    average_order_price = analyzer.calculate_average_price(orders_list)

    folder_name = f'../{output_dir}/run {date.today()} №{randint(1, 10000)}'
    os.makedirs(folder_name, exist_ok=False)

    with open(f'{folder_name}/result.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['order_id', 'product', 'price', 'quantity', 'total'])
        writer.writeheader()
        writer.writerows(orders_list)

    with open(f'{folder_name}/summary.txt', "w", encoding='utf-8') as file:
        file.write(
            f'Количество заказов: {len(orders_list)}\n'
            f'Общая стоимость заказов: {total_orders}\n'
            f'Средняя стоимость заказа: {average_order_price}\n'
        )

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Произошла непредвиденная ошибка -> {e}')
    else:
        print('Программа сработала успешно!')