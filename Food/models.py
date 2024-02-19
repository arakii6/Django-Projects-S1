from django.db import models
# from .utils import generate_slug
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL, null = True, blank = True)
    username = models.CharField(max_length = 150, blank = True, null = True)
    recipe_name = models.CharField(max_length = 100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to = 'recipe_images')
    recipe_view_count = models.PositiveBigIntegerField(default = 0)
    slug = models.SlugField(unique = True, null = True)

    ''' Added the logic in the add_recipe function in views.py
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.recipe_name)
        super(Recipe, self).save(*args, **kwargs)
    '''

    def __str__(self) -> str:
        return self.recipe_name
    
    class Meta:
        verbose_name_plural = 'Recipe'
