def add_time(start, duration, day=None):
    # 1. Parsing the start time:
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # 2. Parsing the duration:
    duration_hour, duration_minute = map(int, duration.split(':'))

    # 3. Conversion of start time to a 24-hour format:
    if period == 'PM' and start_hour != 12:
        start_hour += 12
    elif period == 'AM' and start_hour == 12:
        start_hour = 0

    # 4. Calculation of start time and duration in minutes:
    total_minutes = (start_hour * 60 + start_minute + duration_hour * 60 +
                     duration_minute)

    # 5. Calculation of the new total time:
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    # 6. Determine the period (AM/PM):
    if new_hour < 12:
        new_period = 'AM'
    else:
        new_period = 'PM'

    # 7. Converting the new total time back to a 12-hour format:
    if new_hour == 0:
        new_hour = 12
    elif new_hour > 12:
        new_hour -= 12

    # 8. Formatting of the new total time:
    new_time = f"{new_hour}:{new_minute:02d} {new_period}"

    # 9. Calculation of n days later:
    days_later = total_minutes // (24 * 60)

    # 10. Handling of the optional input (days):
    if day:
        days = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday'
        ]
        start_day_index = days.index(day.capitalize())
        new_day_index = (start_day_index + days_later) % 7
        new_time += f", {days[new_day_index]}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
