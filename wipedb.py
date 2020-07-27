#!/usr/bin/python3


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/SupplyFinder'

man = os.path.join(BASE_DIR, "manage.py")
os.system('rm db.sqlite3')
os.system('rm -rf items/migrations/__pycache__')
os.system('rm items/migrations/0*')
os.system(man+' makemigrations')
os.system(man+' migrate')
os.system(man+' createsuperuser')
