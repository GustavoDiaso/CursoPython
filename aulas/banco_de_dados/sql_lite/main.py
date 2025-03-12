def military_time(time: str) -> str:
    time = time.replace(":", " ")
    splitted_time = time.split(" ")

    hour, minute, period = splitted_time[0], splitted_time[1], splitted_time[2]

    if period == "AM":
        return f"{hour}:{minute}"

    hint = {
        "1": "13",
        "2": "14",
        "3": "15",
        "4": "16",
        "5": "17",
        "6": "18",
        "7": "19",
        "8": "20",
        "9": "21",
        "10": "22",
        "11": "23",
        "12": "12",
    }

    return f"{hint[hour]}:{minute}"


def twenty_four_hour_time(time: str) -> str:
    splitted_time = time.split(":")

    if len(splitted_time[1]) == 1:
        splitted_time[1] = f"0{splitted_time[1]}"

    if int(splitted_time[0]) < 12:
        if int(splitted_time[0]) == 0:
            return f"12:{splitted_time[1]} AM"
        return f"{splitted_time[0]}:{splitted_time[1]} AM"

    hint = {
        "12": "12",
        "13": "1",
        "14": "2",
        "15": "3",
        "16": "4",
        "17": "5",
        "18": "6",
        "19": "7",
        "20": "8",
        "21": "9",
        "22": "10",
        "23": "11",
    }

    return f"{hint[splitted_time[0]]}:{splitted_time[1]} PM"


def add_time(start: str, duration: str, weekday=""):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    military_start = military_time(start)

    extra_hours = 0
    minutes = int(military_start.split(":")[1]) + int(duration.split(":")[1])
    if minutes >= 60:
        extra_hours = minutes // 60
        minutes = minutes % 60

    days = 0
    hours = int(military_start.split(":")[0]) + int(duration.split(":")[0])
    if hours >= 24:
        days = hours // 24
        hours = hours % 24

    if extra_hours != 0:
        hours += extra_hours
        if hours >= 24:
            days += hours // 24
            hours = hours % 24

    twenty_four_hour_start = twenty_four_hour_time(f"{hours}:{minutes}")

    if weekday == "":
        if days == 0:
            return f"{twenty_four_hour_start}"
        elif days == 1:
            return f"{twenty_four_hour_start} (next day)"
        else:
            return f"{twenty_four_hour_start} ({days} days later)"

    else:
        weekday = weekday.strip().capitalize()

        new_weekday_index = days_of_week.index(weekday) + (days % 7)
        if new_weekday_index > 6:
            new_weekday_index -= 7

        new_day_of_week = days_of_week[new_weekday_index]

        if days == 0:
            return f"{twenty_four_hour_start}, {new_day_of_week}"
        if days == 1:
            return f"{twenty_four_hour_start}, {new_day_of_week} (next day)"
        else:
            return f"{twenty_four_hour_start}, {new_day_of_week} ({days} days later)"


print(add_time("8:16 PM", "466:02", "tuesday"))
