import pandas as pd
import user_interface as ui
import models as mod

def main_menu():
    id_menu = ui.main_menu()
    if id_menu == 1:
        mod.add_employee()
    if id_menu == 2:
        search_menu()

def search_menu():
    id_menu = ui.search_menu()
    if id_menu == 1:
        text = ui.direction_input()
        new_df = df_emp.merge(df_direction, left_on='dir_id', right_on='dir_id', how='inner')
        df_filter = new_df['name'].isin([text])
        print(new_df[df_filter])
    if id_menu == 2:
        text = ui.group_input()
        new_df = df_emp.merge(df_group, left_on='grp_id', right_on='grp_id', how='inner')
        df_filter = new_df['name'].isin([text])
        print(new_df[df_filter])    
    if id_menu == 3:
        text = ui.position_input()
        new_df = df_emp.merge(df_position, left_on='pos_id', right_on='pos_id', how='inner')
        df_filter = new_df['name'].isin([text])
        print(new_df[df_filter])
    if id_menu == 4:
        text = ui.status_input()
        new_df = df_emp.merge(df_status, left_on='stat_id', right_on='stat_id', how='inner')
        df_filter = new_df['name'].isin([text])
        print(new_df[df_filter])
    if id_menu == 5:
        text = ui.shift_input()
        new_df = df_emp.merge(df_shift, left_on='shf_id', right_on='shf_id', how='inner')
        df_filter = new_df['name'].isin([text])
        print(new_df[df_filter])

df_emp = pd.read_csv('employee.csv', sep=';', index_col='emp_id')
df_direction = pd.read_csv('direction.csv', sep=';', index_col='dir_id')
df_group = pd.read_csv('group.csv', sep=';', index_col='grp_id')
df_position = pd.read_csv('position.csv', sep=';', index_col='pos_id')
df_status = pd.read_csv('status.csv', sep=';', index_col='stat_id')
df_shift = pd.read_csv('shift.csv', sep=';', index_col='shf_id')


