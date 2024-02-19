# To render the webpage in the front-end
from django.shortcuts import render

#To Add Pagnation
from django.core.paginator import Paginator

# To add OR functionality in Search Bar
from django.db.models import Q

# To preserve the search term while navigating pages.
from django.http import QueryDict

# Sum,Avg e.t.c for aggregate and annotate functions
from django.db.models import *

# Import necessary models
from .models import *

from django.contrib.auth.decorators import login_required

'''----------------------------------------------------------------------'''

# Student List Basic Code: 
'''
def student_details(request):
    queryset = Student.objects.all()

    # Add Search
    if request.GET.get('searchbar'):
        search = request.GET.get('searchbar')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department_name__icontains = search) |
            Q(student_email__icontains = search) 
        )

    # Add Pagination
    paginator = Paginator(queryset, 20)  # Show 20 students per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Preserve search parameters in pagination links
    query_params = QueryDict(mutable=True)
    query_params.update(request.GET)

    context = {'queryset': page_obj, 'query_params': query_params.urlencode()}
    return render(request,'students.html',context) '''

'''----------------------------------------------------------------------'''

# Student List Advanced Code:
# Advanced Search 
def apply_advanced_search(queryset, search_term, search_field):
    if search_term and search_field:
        if search_field == 'name':
            queryset = queryset.filter(student_name__icontains=search_term)
        elif search_field == 'department':
            queryset = queryset.filter(department__department_name__icontains=search_term)
        elif search_field == 'email':
            queryset = queryset.filter(student_email__icontains=search_term)
        # Add more conditions for other fields if needed
    return queryset

'''----------------------------------------------------------------------'''
@login_required(login_url='/sign-in')
# Student List
def student_details(request):
    all_students = Student.objects.all()

    # Add Advanced Search
    search_term = request.GET.get('search_term')
    search_field = request.GET.get('search_field')

    all_students = apply_advanced_search(all_students, search_term, search_field)

    # Add Pagination
    paginator = Paginator(all_students, 20)  # Show 20 students per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Preserve search parameters in pagination links
    query_params = QueryDict(mutable=True)
    query_params.update(request.GET)

    context = {'queryset': page_obj,
               'query_params': query_params.urlencode(),
               'search_term': search_term,
               'page_name':'Student Details'}
    
    return render(request, 'students.html', context)

'''----------------------------------------------------------------------'''

# Show Marks
def show_marks(request,student_id):

    queryset = Subject_Marks.objects.filter(student__studentid__student_id = student_id)

    context = {'queryset':queryset, 'page_name':'Report Card'}
    
    return render(request,'marks.html',context)

'''----------------------------------------------------------------------'''



