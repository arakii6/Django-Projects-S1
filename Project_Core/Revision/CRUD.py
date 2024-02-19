''' 
1. Don't execute this following script !!!
2. This is for revision purpose.
3. Content of this script can be used to learn CRUD operations in Python shell.
4. CRUD = CREATE, READ, UPDATE & DELETE 
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# In Terminal type, 'python manage.py shell' to open python shell
# Then import the models from the app
from Home.models import *

# CREATE
car = Cars(car_name = 'A', speed = 80)
car.save()

# Or we can autosave and avoid using the car.save() function.
# Example 1:
Cars.objects.create(car_name = 'B', speed = 90)

# Example 2:
car_dict = {'car_name': 'C', 'speed': 100}
Cars.objects.create(**car_dict)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# READ - We can access all the created data in MySQL database and also in shell using for loop
car = Cars.objects.all()

for c in car:
    print(c.car_name,c.speed)

'''Must remember!!!
1. Data can be instered into the table both via the shell and MySQL.
2. Incase we insert the data via MySQL, we need to exit() and start the shell again to see the change within the shell.
'''

# Let's make it better with 'f strings'
car = Cars.objects.all()

for c in car:
    print(f'{c.car_name} has a high speed of {c.speed} mph.')

'''
1. As I previously learned, Django automatically adds the 'ID' field to all models.
2. The 'ID' field represents the 'Primary Key' in the tables in MYSQL database.
3. So we can print the ID too.
'''
car = Cars.objects.all()

for c in car:
    print(f'Car number {c.id}, {c.car_name} has a high speed of {c.speed} mph.')

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# UPDATE

# filter() - If a wrong 'ID' is provided, it will return an empty <Query Set []> instead of raising an exception.
Cars.objects.filter(id = 3).update(car_name = 'Nissan', speed = '180')

# get() - If a wrong 'ID' is provided, it will raise the DoesNotExist exception.
car = Cars.objects.get(id = 4)
car.car_name = 'Mercedes'
car.speed = 170
car.save()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# DELETE

# !!! THIS IS DELETE ALL RECORDS !!!
Cars.objects.all().delete() # Be Cautious.

# The right way
Cars.objects.get(id = 1).delete()
# OR
Cars.objects.filter(id=1).delete()

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# IMPORTANT - ways to handle the DoesNotExist exception

# 1 - using try and except
try:
    car = Cars.objects.get(id = 2)
except Cars.DoesNotExist:
    print("Car not found.")
else:
    print("Car found:", car)

# 2 - using the inbuilt 404 exception of Django
from django.shortcuts import get_object_or_404

car = get_object_or_404(Cars, id = 3)
print("Car found:", car)