from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import Recipe

@receiver(post_save, sender = Recipe)
def recipe_added(sender, instance, created, **kwargs):
    
    if created:
        print(f'New Recipe Added: {instance.recipe_name}')
        print(f'Added By: {instance.username}')
    else:
        print(f'Recipe Updated:{instance.recipe_name}')
        print(f'Updated By: {instance.username}')

@receiver(post_delete, sender = Recipe)
def recipe_deleted(sender, instance, **kwargs):
    
    print(f'Recipe Deleted: {instance.recipe_name}')
    print(f'Deleted By: {instance.username}')