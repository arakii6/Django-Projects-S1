# To render html templates in the front end and redirect urls
from django.shortcuts import render,redirect

# To delete respective media files when deletings records
from django.core.files.storage import default_storage

# To use the inbuilt 404 exception of Django when a wrong id is provided while using the get() function
from django.shortcuts import get_object_or_404

# Import respective models to add logic
from .models import Recipe
from .utils import generate_slug

# Django User Authentication Model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout, get_user_model
from django.contrib.auth.decorators import login_required

# Custom User Model
User = get_user_model()

# Django messages framework
from django.contrib import messages

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Recipe Model
@login_required(login_url='/sign-in')
# To Add recipes
def add_recipe(request):
    # Initialize variables
    add_recipe_name = None
    add_recipe_description = None
    add_recipe_image = None

    # Check if the form is submitted (HTTP POST request)
    if request.method == 'POST':
        # Retrieve form data from request.POST and request.FILES
        add_recipe_name = request.POST.get('add_form_recipe_name')
        add_recipe_description = request.POST.get('add_form_recipe_description')
        add_recipe_image = request.FILES.get('add_form_recipe_image')

        UrlSlug = generate_slug(add_recipe_name)
        
        # Create a new Recipe instance in the database
        Recipe.objects.create(
            user = request.user,
            username = request.user.username,
            recipe_name=add_recipe_name,
            recipe_description=add_recipe_description,
            recipe_image=add_recipe_image,
            slug = UrlSlug
        )

        # Redirect to the '/recipes' page after successful form submission
        return redirect('/recipes')

    # Retrieve all recipes from the database
    queryset = Recipe.objects.all()

    # Filter recipes based on search query (HTTP GET request)
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    # Prepare context for rendering the template
    context = {'recipes': queryset, 'page_name': 'Recipe Form'}

    # Render the 'main/recipes.html' template with the provided context
    # Context is used to send data from backend to frontend
    return render(request, 'main/recipes.html', context)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# To Update recipes
def update_recipe(request,url_slug):
    
    # Retrieve the recipe instance
    queryset = get_object_or_404(Recipe, slug = url_slug) # Instead of using, queryset = Recipe.objects.get(id = ID)

    if request.method == 'POST':
        update_recipe_name = request.POST.get('update_form_recipe_name')
        update_recipe_description = request.POST.get('update_form_recipe_description')
        update_recipe_image = request.FILES.get('update_form_recipe_image')

        # Update the recipe instance
        queryset.recipe_name = update_recipe_name
        queryset.recipe_description = update_recipe_description
        
        if update_recipe_image:
            queryset.recipe_image = update_recipe_image
        
        queryset.save()

        ''' Not needed atm as all new entries will be created with logged in user data
        if not queryset.user:
            queryset.user = request.user
            queryset.username = request.user.username
            queryset.save()'''

        return redirect('/recipes')

    context = {'recipe':queryset,'page_name':'Update Recipe'}
    return render(request,'main/update_recipe.html',context)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# To Delete recipes
def delete_recipe(request,ID):
    
    # Retrieve the recipe instance
    queryset = get_object_or_404(Recipe, id = ID)

    # Get the path to the media file and 
    media_path = queryset.recipe_image.path
    
    # Delete the associated media file
    if default_storage.exists(media_path):
        default_storage.delete(media_path)
    
    # Delete the recipe from the database
    queryset.delete()
    
    return redirect('/recipes')

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# User Registration
def register(request):
    # Initialize variables to None
    add_first_name = None
    add_last_name = None
    add_username = None
    add_password = None

    # Check if the form is submitted (HTTP POST request)
    if request.method == 'POST':
        # Retrieve form data from request.POST
        add_first_name = request.POST.get('register-form_firstname')
        add_last_name = request.POST.get('register-form_lastname')
        add_username = request.POST.get('register-form_username')
        add_password = request.POST.get('register-form_password')

        # Check if the submitted username is unique
        if User.objects.filter(username=add_username).exists():
            # If the username already exists, show a warning message and redirect back to the registration page
            messages.warning(request, "Username Exists. Please enter a different username.")
            return redirect('register_page')
        
        else:
        # Create and save the user instance with the submitted data
            user_obj = User.objects.create(
                first_name = add_first_name,
                last_name = add_last_name,
                username = add_username
            )
            user_obj.set_password(add_password)
            user_obj.save()

            # Display a success message and redirect to the login page
            messages.success(request, "Account created successfully.")
            return redirect('register_page')

    # Render the registration page (register.html)
    context = {'page_name': 'Register Account'}
    return render(request, 'main/register.html', context)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# User Sign-In
def sign_in(request):
    # Check if the form is submitted (HTTP POST request)
    if request.method == 'POST':
        # Retrieve form data from request.POST
        add_username = request.POST.get('sign-in-form_username')
        add_password = request.POST.get('sign-in-form_password')

        # Check if the username exists in the database
        if not User.objects.filter(username=add_username).exists():
            messages.warning(request, "Username Invalid. Please try again.")
            return redirect('sign_in_page')

        else:
            # Authenticate the user with the provided username and password.
            # The Authenticate function is used as the stored password is encrypted.
            user = authenticate(username=add_username, password=add_password)

            if user:
                # Authentication succeeded, user is a valid User object. This also starts the user's session.
                login(request, user)
                return redirect('recipe_page')
            else:
                # Authentication failed, user is None
                messages.warning(request, "Invalid login credentials. Please try again.")
                return redirect('sign_in_page')

    # Render the sign-in page (sign-in.html) if the request method is not POST
    context = {'page_name': 'Sign In'}
    return render(request, 'main/sign-in.html', context)

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# User Sign-Out
def sign_out(request):
    logout(request)
    return redirect('sign_in_page')