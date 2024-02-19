from django.shortcuts import render, redirect
from .forms import TestForm

def add_test_item(request):
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_test_item')
    else:
        form = TestForm()

    return render(request, 'add_test_item.html', {'form': form})
