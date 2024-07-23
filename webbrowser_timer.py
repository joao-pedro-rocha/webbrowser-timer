import webbrowser
from time import sleep
import re
import pymsgbox


# Display instruction for time format
def warning_message():
    print('Set time in HH:MM:SS format!\n')


# receives the entered time and converts it into seconds
def set_time():
    while True:
        time_str = str(input('Set a time (HH:MM:SS):'))\
            .replace(' ', '')

        if len(re.findall('[a-z]', time_str)) > 0:
            warning_message()
            continue

        if len(time_str) != 8:
            warning_message()
            continue

        break

    time_str = time_str.replace(':', '')
    hours = int(time_str[:2])
    minutes = int(time_str[2:4])
    seconds = int(time_str[4:])
    total_seconds = (hours * 3600) + (minutes * 60) + seconds

    return total_seconds


# waits for the chosen time and displays a message when the time is up
def times_up(time):
    sleep(time)
    pymsgbox.alert(text='Time is over!', title='Time is over!')


while True:
    print('''\n***WEBBROWSER TIMER***
MENU:
[1] Start
[2] Exit''')
    # TODO fazer alguma validacao de url
    menu_option = input('Enter an option: ').replace(' ', '')

    # asks for a url, a time, opens the browser, counts the time and then
    # displays a message
    if menu_option == '1':
        url = str(input('Enter a url: '))

        # TODO comparar o horario do usuario apenas com  o horario do datetime
        # convertido em string para parar o programa
        time = set_time()
        webbrowser.open_new_tab(url)
        times_up(time)

        print('''***\nWEBBROWSER TIMER***
MENU:
[1] Continue
[2] Back''')
        menu_option = input('Enter an option: ').replace(' ', '')
        while True:
            # asks for the time and at the end displays a message
            if menu_option == '1':
                time = set_time()
                times_up(time)
                menu_option = input('Enter an option: ').replace(' ', '')
                # return to the main menu
            elif menu_option == '2':
                break
            else:
                print('Enter a valid option!\n')
                menu_option = input('Enter an option: ').replace(' ', '')

    # exit the program
    elif menu_option == '2':
        break
    else:
        print('Enter a valid option!\n')
