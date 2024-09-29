while True:
     try:
         current_hour = int(input('What is the current time in hours (0-23)? '))
         if current_hour < 0 or current_hour > 23:
             raise ValueError()
         break
     except ValueError:
          print('Oops! That was not a valid number.  Try again...')

while True:
     try:
        alarm_hours = int(input('How many hours do you wnat to wait for the alarm? '))
        break
     except ValueError:
         print('Oops! That was not a valid number.  Try again...')

hours_to_add = alarm_hours % 24

new_time = int((current_hour + hours_to_add) % 24)

print(f'Your alarm will ring at {new_time:02}:00')