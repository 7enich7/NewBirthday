from datetime import date


month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day0 = date(2006, 1, 1)
a = 0
mm = 1
name_month = ''


print('Введите месяц рождения младшего партнёра')
date1_month = int(input())
print('Введите день рождения младшего партнёра')
date1_day = int(input())

print('Введите месяц рождения старшего партнёра')
date2_month = int(input())
print('Введите день рождения старшего партнёра')
date2_day = int(input())

date1 = date(2006, date1_month, date1_day)
date2 = date(2006, date2_month, date2_day)


def num_day(date1, date2):
    if date1 > date2:
        d1d2 = (date1 - date2).days
        return d1d2
    else:
        d1d2 = (date2 - date1).days
        return d1d2


mid_day = num_day(date1, date2)
if mid_day > 182.5:
    day_of_year = (date2 - day0).days
    day = ((mid_day / 2) + day_of_year) + 1
else:
    day_of_year = (date1 - day0).days
    day = (((365 - mid_day) / 2) + day_of_year) + 1


if day > 365: day -= 365


for i in range(len(month_list)):
    if month_list[i] + a < day:
        a += month_list[i]
        mm += 1

dayday = day - a - 1

if mm == 1:
    name_month += 'января'
elif mm == 2:
    name_month += 'февраля'
elif mm == 3:
    name_month += 'марта'
elif mm == 4:
    name_month += 'апреля'
elif mm == 5:
    name_month += 'мая'
elif mm == 6:
    name_month += 'июня'
elif mm == 7:
    name_month += 'июля'
elif mm == 8:
    name_month += 'августа'
elif mm == 9:
    name_month += 'сентября'
elif mm == 10:
    name_month += 'октября'
elif mm == 11:
    name_month += 'ноября'
elif mm == 12:
    name_month += 'декабря'


print(int(day), 'New Happy Birthday')
print(f'{int(dayday)}-го {name_month}')
