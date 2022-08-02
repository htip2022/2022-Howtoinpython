#!/usr/bin/env python3

# Arrival Calculator


""" *Speed formula*
v = distance/time"""

import datetime


def arrivalCalculator(departDate, departTime, distance, speed):
    # Convert departDate and departTime into datetime format
    depart = datetime.datetime.strptime(departDate, '%Y-%m-%d').date()
    departTime_conv = datetime.datetime.strptime(departTime, '%I:%M %p')
    # Join depart and timedepart
    depart_dateTime = datetime.datetime(depart.year, depart.month, depart.day, departTime_conv.hour,
                                        departTime_conv.minute)
    # Calculate hours and minutes throught t=d/v
    durationTrip = distance / speed
    # Convert durationTrip into datetime format
    durationTrip_delta = datetime.timedelta(hours=durationTrip)
    arrival_dateTime = depart_dateTime + durationTrip_delta
    arrivalDate = datetime.date(arrival_dateTime.year, arrival_dateTime.month, arrival_dateTime.day)
    arrivalTime = (datetime.time(arrival_dateTime.hour, arrival_dateTime.minute)).strftime('%I:%M %p')
    print(f'Arrival date: {arrivalDate}\nTime Arrival: {arrivalTime}')


def main():
    print('Arrival Calculator\n')
    # Set user's variables
    departDate = input('Enter the departure date (YYYY-MM-DD): ')  # 2022-07-29
    departTime = input('Enter the departure time (HH:MM AM/PM): ')  # 09:00 PM
    distance = float(input('Enter the distance [km]: '))  # 9373 km (5824 mi)
    speed = float(input('Enter km/hour: '))  # 885 y 933 kmph (550 y 580 mph)

    arrivalCalculator(departDate, departTime, distance, speed)

    while input("\nContinue? (y/n): ") == "y":
        departDate = input('Enter the departure date (YYYY-MM-DD): ')  # 2022-07-31
        departTime = input('Enter the departure time (HH:MM AM/PM): ')  # 11:50 PM
        distance = float(input('Enter the distance [km]: '))  # 1500 km (5824 mi)
        speed = float(input('Enter km/hour: '))  # 885 y 933 kmph (550 y 580 mph)

        arrivalCalculator(departDate, departTime, distance, speed)
    else:
        print('Bye!')


if __name__ == '__main__':
    main()