def add_time(start, duration, day):

    start = start.split(":")
    hour_start = int(start[0])
    minutes_start = int(start[1].split()[0])
    period_start = start[1].split()[1]

    duration = duration.split(":")
    hour_duration = int(duration[0])
    minutes_duration = int(duration[1])
    period = ""

    new_hour = hour_start
    new_minutes = minutes_start + minutes_duration
    if new_minutes >= 60:
        new_hour += new_minutes // 60
        new_minutes = new_minutes % 60

    new_hour += hour_duration

    days = new_hour // 24
    if new_hour > 12:
        if period_start == "PM":
            period = "AM"
        elif period_start == "AM":
            period = "PM"

        new_hour = new_hour % 12

    if days > 0:
        days += 1
        if days == 1:
            new_time = (
                f"{str(new_hour)}:{str(new_minutes).zfill(2)} {period} (next day)"
            )
        else:
            new_time = f"{str(new_hour)}:{str(new_minutes).zfill(2)} {period} ({days} days later)"
    elif days == 0:
        new_time = f"{str(new_hour)}:{str(new_minutes).zfill(2)} {period}"

    return new_time
