def get_WeekDay(y, absday):
    delta_year = y - 1901
    falseleaps = 0
    for dy in range(int(y / 100) - 19):
        if dy % 4 == 0: continue
        falseleaps += 1
    leap_count = int(delta_year / 4) - falseleaps
    weekday = (leap_count * 366 + (delta_year - leap_count) * 365 + absday) % 7
    return weekday

def get_FirtDays(y):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = False
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0): leap = True
    if leap: days[1] = 29
    first_absdays = [1]
    for daycount in days:
        first_absdays.append(first_absdays[-1] + daycount)
    first_absdays.pop()
    return first_absdays

count = 0
for y in range(1901, 2001):
    for fd in get_FirtDays(y):
        if get_WeekDay(y, fd) == 6: count += 1

print(count)