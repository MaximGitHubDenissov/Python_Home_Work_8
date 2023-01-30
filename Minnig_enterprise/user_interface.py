
def direction_input():
    name = input('Enter direction name: ')
    return name

def group_input():
    name = input('Enter group name: ')
    return name

def position_input():
    name = input('Enter position name: ')
    return name

def shift_input():
    name = input('Enter shift name: ')
    return name

def status_input():
    name = input('Enter status name:  ')
    return name

def first_name_input():
    name = input('Enter first_name: ')
    return name

def second_name_input():
    name = input('Enter second name:  ')
    return name

def birth_date_input():
    date = input('Enter birthdate: ')
    return date

def direction_select(list):
    print('You can appoint employee in next Directions: ')
    print(list, sep='\n')
    print('Enter direction ID: ')
    id = input(': ')
    return id

def group_select(list):
    print('You can appoint employee in next Groups: ')
    print(list, sep='\n')
    print('Enter group ID: ')
    id = input(': ')
    return id

def position_select(list):
    print('You can appoint employee in next positions: ')
    print(list, sep='\n')
    print('Enter position ID: ')
    id = input(': ')
    return id

def salary_input():
    print('Enter salary for employee')
    sal = input(': ')
    return sal

def shift_select(list):
    print('You can appoint employee to next shifts: ')
    print(list, sep='\n')
    print('Enter shift ID: ')
    id = input(': ')
    return id

def status_select(list):
    print('You set employee next status: ')
    print(list, sep='\n')
    print('Enter status ID: ')
    id = input(': ')
    return id

def error():
    print('Not valid choice!')

def main_menu():
    print('You are in main menu (employees data base)\n\
        Please make your choice:\n\
        1 - Add employee\n\
        2 - Search menu')
    res = int(input(': '))
    return res

def search_menu():
    print('You are in search menu. Your choice: \n\
        1 - Filter employee on directions\n\
        2 - Filter employee on group\n\
        3 - Filter employee on position\n\
        4 - Filter employee on status\n\
        5 - Filter employee on shift')
    res = int(input(': '))
    return res