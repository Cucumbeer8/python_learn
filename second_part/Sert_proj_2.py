def add_time(start, duration, day=''):
    time_now, meridiem = start.split()
    start_hour, start_minute = map(int, time_now.split(':'))
    duration_hour, duration_minute = map(int, duration.split(':'))

    if meridiem == 'PM':
        start_hour += 12
    sum_minute = start_minute + duration_minute
    sum_hour = start_hour + duration_hour + (sum_minute // 60)
    end_minute = sum_minute % 60
    end_hours = sum_hour % 24

    day_of_week, how_much_day = days(sum_hour, day)

    if end_hours >= 12 :
        end_meridiem = 'PM'
        if end_hours > 12:
            end_hours -= 12
    else:
        end_meridiem = 'AM'
        if end_hours == 0:
            end_hours = 12

    if how_much_day > 1:
        how_much_day_output = f" ({how_much_day} days later)"
    elif how_much_day == 1:
        how_much_day_output = f" (next day)"
    else:
        how_much_day_output = ""

    new_time = f"{end_hours}:{end_minute:02d} {end_meridiem}{day_of_week}{how_much_day_output}"

    return new_time


def days(hours, day=''):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_of_week = ''
    how_much_day = hours // 24

    if day:
        day = day.capitalize()
        day_of_week_index = days.index(day)
    else:
        day_of_week_index = None

    if day_of_week_index is not None:
        day_of_week_index = (day_of_week_index + how_much_day) % 7
        day_of_week = days[day_of_week_index]
        day_of_week_output = f", {day_of_week}"
    else:
        day_of_week_output = ''

    return day_of_week_output, how_much_day



add_time('2:59 AM', '24:00')