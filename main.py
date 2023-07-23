from check_date import check_date
from chess import check_beat, generate_positions
from sys import argv

# print(check_date(input('Введите дату в формате DD.MM.YYYY: ')))
# check_date(argv[1])

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [7, 4, 2, 8, 6, 1, 3, 5]

print(check_beat(x, y))
# generate_positions()