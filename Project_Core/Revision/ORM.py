# ORM_revision.py

'''
1. Don't execute this following script !!!
2. This is for revision purpose.
3. Content of this script can be used to learn Django ORM queries.
'''

# Import the Recipe model
from Food.models import Recipe

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# 1. Retrieve all objects from the Recipe model
recipe_obj = Recipe.objects.all()

# 2. Access a specific object in the QuerySet
recipe_obj[0]

# 3. Access a specific field of an object
recipe_obj[0].recipe_view_count

# 4. Update a field for each object in the QuerySet
import random

for recipe in recipe_obj:
    recipe.recipe_view_count = random.randint(10, 100)
    recipe.save()

# 5. Order objects by a specific field in ascending order
recipe_obj = Recipe.objects.all().order_by('recipe_view_count')

# 6. Order objects by a specific field in descending order
recipe_obj = Recipe.objects.all().order_by('-recipe_view_count')

# 7. Retrieve a subset of objects (slicing). Similar to Limit By in SQL
recipe_obj = Recipe.objects.all().order_by('-recipe_view_count')[0:2]

# 8. Filter objects based on a condition (greater than or equal)
recipe_obj = Recipe.objects.filter(recipe_view_count__gte=50)

# 9. Filter objects based on a condition (less than or equal)
recipe_obj = Recipe.objects.filter(recipe_view_count__lte=50)

# 10. To see the specific output of the data, use indexing
recipe_obj[0].recipe_view_count
