dayOfWeeks = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
str_DayOfWeeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def add_time(start, duration, dayOfWeek=None):
    # Split Start
    new_time = ""
    time = start.split(' ')
    time_str = time[0].split(':')

    # Cur time (Plus all two input)
    cur_hour = 0
    cur_minute = 0

    # Hour, minute of start
    hour = int(time_str[0])
    minute = int(time_str[1])

    if time[1] == "PM":
        cur_hour = hour + 12

    # Hour, minute of duration
    duration_str = duration.split(':')
    duration_hour = int(duration_str[0])
    duration_minute = int(duration_str[1])

    # Plus All
    cur_hour += duration_hour
    cur_minute = minute + duration_minute

    if cur_minute >= 60:
        cur_minute %= 60
        cur_hour += 1

    date_plus = cur_hour / 24
    hour_Day = cur_hour % 24

    print("Date Plus " + str(date_plus))
    print("Hour Day " + str(hour_Day))
    print("Minute " + str(cur_minute))

    str_Tail = "AM"

    if hour_Day >= 12:
        hour_Day %= 12
        str_Tail = "PM"

    new_time = str(hour_Day) + ":" + str(cur_minute) + " " + str_Tail

    if dayOfWeek:
        for i in range(0, len(dayOfWeeks)):
            if dayOfWeeks[i] == str(dayOfWeek).upper():
                new_time += ' ' + str_DayOfWeeks[int(i + date_plus) % 7]

    if 24 <= cur_hour < 48:
        new_time += ' (next day)'
    elif int(date_plus) >= 1:
        new_time += ' ' + '(' + str(int(date_plus)) + ' days later)'

    # hour = int(time[0])
    # minute = int(time[2])

    return new_time

if __name__ == '__main__':
    print(add_time("11:30 AM", "2:32", "Monday"))
