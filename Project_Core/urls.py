"""
URL configuration for Project_Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home.views import *
from Accounts.views import *
from Food.views import *
from Test_App.views import add_test_item

urlpatterns = [

    # Home App
    path('', home, name = 'home_page'),
    path('success', success, name = 'success_page'),
    path('about', about, name = 'about_page'),
    path('contact', contact, name = 'contact_page'),

    # Food App
    path('recipes', add_recipe, name = 'recipe_page'),
    path('update_recipe/<url_slug>/', update_recipe, name = 'update_recipe'),
    path('delete_recipe/<ID>/', delete_recipe, name = 'delete_recipe'),
    ## Auth
    path('register', register, name = 'register_page'),
    path('sign-in', sign_in, name = 'sign_in_page'),
    path('sign-out', sign_out, name='sign_out_page'),

    # Test App
    path('add-test-item', add_test_item, name='add_test_item'),

    # Accounts App
    path('student-details',student_details,name='student_details_page'),
    path('report-card/<student_id>',show_marks,name='report_card_page'),

    # Django Admin
    path('admin', admin.site.urls),
]


# Serve media files during development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()