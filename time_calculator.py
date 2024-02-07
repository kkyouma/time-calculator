def sum_time(x, y):
    return x + y


def add_time(start, duration):

    start = start.split(":")
    hour_start = int(start[0])
    minutes_start = int(start[1].split()[0])
    period_start = start[1].split()[1]

    duration = duration.split(":")

    hour_duration = int(duration[0])
    minutes_duration = int(duration[1])

    period = ""

    new_minutes = sum_time(minutes_start, minutes_duration)
    new_hour = hour_start
    if new_minutes >= 60:
        new_hour += new_minutes // 60
        new_minutes = new_minutes % 60

    new_hour = sum_time(hour_start, hour_duration)

    if new_hour >= 12:
        if period_start == "PM":
            period = "AM"
        elif period_start == "AM":
            period = "PM"

        new_hour = new_hour % 12

    new_time = f"{new_hour}:{new_minutes} {period}"

    return new_time


add_time("11:06 PM", "2:02")
