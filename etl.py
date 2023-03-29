from services.postgres import bulk_data
import os

list_files = ['employees.csv', 'departments.csv', 'jobs.csv']

path = os.path.join(os.getcwd(), 'resources')

for item_file in list_files:
    new_path = os.path.join(path, item_file)
    bulk_data(new_path, item_file.split('.')[0])
