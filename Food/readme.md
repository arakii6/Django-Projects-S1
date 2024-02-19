# Understanding the Food Project - README
Remember to regularly review and update your README as your project evolves. Clear documentation makes it easier for collaborators and contributors to understand and contribute to your project.


## Step 1: Build the Recipe Model in models.py
1. In `models.py`, define the Recipe model by specifying column names and their respective data types to be stored in MySQL, essentially creating a table structure.
2. Run `python manage.py makemigrations` to create migration files that capture the changes in the model.
3. Execute `python manage.py migrate` to apply these changes to the MySQL database.
   - **Note:** Any future edits to the model require running `makemigrations` and `migrate` to update the database accordingly.


## Step 2: Create the HTML template for the Recipe Form
1. Navigate to the `templates` folder, Django's default template engine location.
2. Create the `recipes.html` file to serve as the template for the Recipe Form.
3. Inside `recipes.html`, design the structure of the recipe form. Options include copying a form template from getBootstrap or using ChatGPT to generate one with custom styling.
4. As a backend developer, ensure the HTML file includes the necessary code for data collection and display.
   - Add `method="post"` to the form tag to indicate form submissions via the POST method.
   - If the form involves file uploads, include `enctype="multipart/form-data"` in the form tag.
   - Insert `{% csrf_token %}` just below the form tag to mitigate Cross-Site Request Forgery (CSRF) attacks.
     - CSRF is a security measure against malicious websites attempting unauthorized actions on behalf of authenticated users.
   - Ensure each label corresponds to the appropriate input type and name, aligning with the model definition in `models.py` and data processing in `views.py`.
      - **Important Note:** While the name field in the label tag of the form, the variable names in `views.py`, and the field names in `models.py` don't have direct dependencies, it's crucial to maintain consistency. Please make sure to map them accordingly in `views.py` to ensure proper data processing and storage.


## Step 3: Create the Logic in `views.py`

1. **Import Necessary Modules:**
   - Import essential modules and functions needed for the logic:
     ```python
     from .models import Recipe
     from django.shortcuts import render, redirect, get_object_or_404
     from django.core.files.storage import default_storage
     ```

2. **Create a Function to Add Recipes (`add_recipe`):**
   - Define a function to handle the addition of new recipes and pass `request` as a parameter.

3. **Initialize Variables:**
   - Inside the function, initialize three variables (`add_recipe_name`, `add_recipe_description`, and `add_recipe_image`) as `None`. This is a good practice to ensure fresh storage of form data.

4. **Check for HTTP POST Request:**
   - Use an `if statement` to check if the current request method is `POST`. This is common when handling form submissions.

5. **Retrieve Form Data:**
   - If it's a `POST` request, retrieve form data (recipe name, description, and image) from `request.POST` and `request.FILES`.
     - Use `request.POST.get('label_name')` to capture user-entered data and store it in the respective variables.
     - Utilize `request.FILES.get('file name')` to store file-type data in the corresponding variable.

6. **Create a New Recipe Instance in the Database:**
   - Use the retrieved form data to create a new instance of the `Recipe` model in the database. This involves adding a new record with the provided recipe details.
     - Example: `Recipe.objects.create(model_fields=respective_variables)`

7. **Redirect After Form Submission:**
   - Redirect to the '/recipes' page after successfully submitting the form, all within the `if statement`. This ensures a smooth user experience.

8. **Prepare Context for Rendering:**
   - Add essential key-value pairs to the context dictionary. Common keys include 'recipes' (for the list of recipes) and 'page_name' (indicating the current page).

9. **Render the Template:**
   - Use the `render` function, passing in the `request` parameter, HTML template file path, and the context dictionary. This renders the complete view in the frontend.

