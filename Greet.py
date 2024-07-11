import time
timestamp=time.strftime('%H:%M:%S')
times = time.strftime('%I:%M %p')
name=input('Enter your name: ')
def Greet():
    if timestamp < '12:00:00':
        print(f'Good Morning, {name}! It is currently {times}')

    elif timestamp < '18:00:00':
        print(f'Good Afternoon, {name}! It is currently {times}')

    elif timestamp < '21:00:00':
        print(f'Good Evening, {name}! It is currently {times}')

    else:
        print(f'Good Night, {name}! It is currently {times}')

Greet()