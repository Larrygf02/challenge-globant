from services.postgres import bulk_data
import os

list_files = ['hired_employees.csv']

path = os.path.join(os.getcwd(), 'resources')

for one_file in list_files:
    new_path = os.path.join(path, 'hired_employees.csv')
    bulk_data(new_path)
