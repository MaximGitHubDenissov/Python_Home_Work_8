import csv
import user_interface as ui
# DB creation models
def create_employee_db():
    with open('employee.csv', 'w') as file:
        headers = ['emp_id', 'first_name', 'second_name', 'birth_date',\
             'dir_id', 'grp_id', 'pos_id', 'salary', 'shf_id', 'stat_id']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';',lineterminator='\n')
        writer.writeheader()

def create_direction_db():
    with open('direction.csv', 'w') as file:
        headers = ['dir_id', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writeheader()

def create_group_db():
    with open('group.csv', 'w') as file:
        headers = ['grp_id', 'name', 'dir_id']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writeheader()

def create_position_db():
    with open('position.csv', 'w') as file:
        headers = ['pos_id', 'name', 'grp_id'] 
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writeheader()

def create_shift_db():
    with open('shift.csv', 'w') as file:
        headers = ['shft_id', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writeheader()

def create_status_db():
    with open('status.csv', 'w') as file:
        headers = ['stat_id', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writeheader()
#-----------------------------------------------------------------------------------------------------
# last_ID storage

def dir_id():
    with open('dir_id.txt', 'r') as file:
        for line in file:
            id = int(line)
            id+=1
    with open('dir_id.txt', 'w') as file:
        file.write(str(id))
    return id

def grp_id():
    with open('grp_id.txt', 'r') as file:
        for line in file:
            id = int(line)
            id+=1
    with open('grp_id.txt', 'w') as file:
        file.write(str(id))
    return id

def pos_id():
    with open('pos_id.txt', 'r') as file:
        for line in file:
            id = int(line)
            id+=1
    with open('pos_id.txt', 'w') as file:
        file.write(str(id))
    return id

def shf_id():
    with open('shf_id.txt', 'r') as file:
         for line in file:
            id = int(line)
            id+=1
    with open('shf_id.txt', 'w') as file:
        file.write(str(id))
    return id

def sts_id():
    with open('sts_id.txt', 'r') as file:
        for line in file:
            id = int(line)
            id+=1
    with open('sts_id.txt', 'w') as file:
        file.write(str(id))
    return id

def emp_id():
    with open('emp_id.txt', 'r') as file:
        for line in file:
            id = int(line)
            id+=1
    with open('emp_id.txt', 'w') as file:
        file.write(str(id))
    return id
#-----------------------------------------------------------------------------------------------------
# Add uniq positions (admin rights)

def add_direction():
    with open('direction.csv', 'a+') as file:
        headers = ['ID', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'ID': str(dir_id()), 'name': ui.direction_input()})
        
def add_group():
    with open('group.csv', 'a+') as file:
        headers = ['ID', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'ID': str(grp_id()), 'name': ui.group_input()})

def add_position():
    with open('position.csv', 'a+') as file:
        headers = ['ID', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'ID': str(pos_id()), 'name': ui.position_input()})
    
def add_shift():
    with open('shift.csv', 'a+') as file:
        headers = ['shft_id', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'shft_id': str(shf_id()), 'name': ui.shift_input()})

def add_status():
    with open('status.csv', 'a+') as file:
        headers = ['stat_id', 'name']
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'stat_id': str(sts_id()), 'name': ui.status_input()})
#------------------------------------------------------------------------------------------------------
# add employee (user right)

def add_employee():
    with open('employee.csv', 'a+') as file:
        headers = ['emp_id', 'first_name', 'second_name', 'birth_date', 'dir_id', 'grp_id','pos_id',\
            'salary', 'shf_id', 'stat_id']
        first_name = ui.first_name_input()
        second_name = ui.second_name_input()
        birth_date = ui.birth_date_input()
        dir_id, grp_id, pos_id = direction_select()
        writer = csv.DictWriter(file, fieldnames=headers, delimiter=';', lineterminator='\n')
        writer.writerow({'emp_id': str(emp_id()), 'first_name': first_name,\
            'second_name': second_name, 'birth_date': birth_date,\
                'dir_id': dir_id, 'grp_id': grp_id, 'pos_id': pos_id, 'salary': ui.salary_input(),\
                    'shf_id': shift_select(), 'stat_id': status_select()})

def direction_select():
    with open('direction.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        res = []
        for row in reader:
            res.append(row['dir_id'])
            res.append(row['name']) 
    
    while True:
        dir_id = ui.direction_select(res)
        if dir_id in res and dir_id.isdigit():
            res_1 = dir_id
            break
        else:
            ui.error()
    res_2 = group_select(res_1)
    res_3 = position_select(res_2)
    return res_1, res_2, res_3

def group_select(dir_id):
    with open('group.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        res = []
        for row in reader:
            if row['dir_id'] == dir_id:
                res.append(row['grp_id'])
                res.append(row['name'])
    while True:
        grp_id = ui.group_select(res)
        if grp_id in res and grp_id.isdigit():
            return grp_id
        else:
            ui.error()

def position_select(grp_id):
    with open('position.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        res = []
        for row in reader:
            if row['grp_id'] == grp_id:
                res.append(row['pos_id'])
                res.append(row['name'])
    while True:
        pos_id = ui.position_select(res)
        if pos_id in res and pos_id.isdigit():
            return pos_id
        else:
            ui.error()

def shift_select():
    with open('shift.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        res = []
        for row in reader:
                res.append(row['shf_id'])
                res.append(row['name'])
    while True:
        pos_id = ui.shift_select(res)
        if pos_id in res and pos_id.isdigit():
            return pos_id
        else:
            ui.error()

def status_select():
    with open('status.csv', 'r') as f:
        reader = csv.DictReader(f, delimiter=';')
        res = []
        for row in reader:
                res.append(row['stat_id'])
                res.append(row['name'])
    while True:
        pos_id = ui.status_select(res)
        if pos_id in res and pos_id.isdigit():
            return pos_id
        else:
            ui.error()


