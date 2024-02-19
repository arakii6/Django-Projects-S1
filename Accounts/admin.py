from django.contrib import admin
from django.db.models import Sum
from .models import *

# Register your models here.
admin.site.register(Department)
admin.site.register(StudentId)
admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Purchase)
admin.site.register(Subject)

# Define a custom admin for Subject_Marks
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

# Register the custom admin for Subject_Marks
admin.site.register(Subject_Marks, SubjectMarksAdmin)


# Define a custom admin for Report_Card
class ReportCardAdmin(admin.ModelAdmin):
    def total(self, obj):
        queryset = Subject_Marks.objects.filter(student = obj.student)
        total_marks = queryset.aggregate(sum_of_marks=Sum('marks'))
        return total_marks['sum_of_marks']

    list_display = ['student','total','rank','date']
    ordering = ['rank']

# Register the custom admin for Report_Card
admin.site.register(Report_Card, ReportCardAdmin)