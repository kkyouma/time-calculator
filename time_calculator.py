def add_time(start, duration, week_day=None):
    week_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    if week_day:
        week_day = week_day.capitalize()
        index_day = week_days.index(week_day)

    start = start.split(":")
    hour_start = int(start[0])
    minutes_start = int(start[1].split()[0])
    period_start = start[1].split()[1]

    duration = duration.split(":")
    hour_duration = int(duration[0])
    minutes_duration = int(duration[1])
    period = period_start

    new_hour = hour_start + hour_duration
    new_minutes = minutes_start + minutes_duration

    if new_minutes >= 60:
        new_hour += new_minutes // 60
        new_minutes = new_minutes % 60

    days = new_hour // 24

    if new_hour >= 12:
        if period_start == "PM" and new_hour % 13 != 0:
            period = "AM"
            days += 1
        elif period_start == "AM" and new_hour % 13 != 0:
            period = "PM"

        if new_hour > 12:
            new_hour %= 12

    if week_day:
        new_index_day = (index_day + days) % 7
        day = f", {week_days[new_index_day]}"
    else:
        day = ""

    time = f"{new_hour}:{str(new_minutes).zfill(2)}"

    if days == 0:
        new_time = f"{time} {period}{day}"
    elif days == 1:
        new_time = f"{time} {period}{day} (next day)"
    else:
        new_time = f"{time} {period}{day} ({days} days later)"

    return new_time
