import math

current_hour = int(input('What is the current time in hours (0-23)?'))
alarm_hours = int(input('How many hours do you wnat to wait for the alarm?'))

hours_to_add = alarm_hours % 24

new_time = int((current_hour + hours_to_add) % 23)

print(f'Your alarm will ring at {new_time:02}:00')