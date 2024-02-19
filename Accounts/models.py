# Import necessary module
from django.db import models

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

'''-------------------------------------------------------------------------------------------------'''

# Department Class
class Department(models.Model):

    department_name = models.CharField(max_length=100)
    student_count = models.PositiveIntegerField(default=0,null=True)

    def __str__(self) -> str:
        return self.department_name
    
    # Define the default ordering for queries. Add ['-department'] for descending.
    class Meta:
        ordering = ['department_name']
        verbose_name_plural = "Department"

'''-------------------------------------------------------------------------------------------------'''

# Student ID Class
class StudentId(models.Model):

    student_id = models.CharField(max_length=100)

    '''
    Override Django's default string representation to define how the object
    appears in Django's admin interface. In this case, we use the student_id
    as the display name for instances of the StudentId model.'''
    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        verbose_name_plural = 'Student Id'

'''-------------------------------------------------------------------------------------------------'''

# Student Class
class Student(models.Model):

    # Define a ForeignKey relationship to the Department model, with a related name 'depart'
    department = models.ForeignKey(Department, related_name='stdt_dept', on_delete=models.CASCADE)
    
    # Define a OneToOneField relationship to the StudentId model, with a related name 'student_id'
    studentid = models.OneToOneField(StudentId, related_name='stdt_id', on_delete=models.SET_NULL, null=True)
    
    # Define fields for student information
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.PositiveBigIntegerField(default=18)
    student_address = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    # Student Manager class
    objects = StudentManager()
    admin_objects = models.Manager()


    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        
        '''
        Override Django's default string representation to define how the model
        appears in Django's admin interface. In this case, we use the 'student'
        as the display name for the model.'''
        verbose_name_plural = "Student"

'''-------------------------------------------------------------------------------------------------'''

# Subject Class
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    # student = models.ForeignKey(Student,related_name='stdt_subject',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subject_name

'''-------------------------------------------------------------------------------------------------''' 

# Marks Class
class Subject_Marks(models.Model):
    student = models.ForeignKey(Student,related_name='stdt_marks',on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,related_name='subject_marks',on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'Name: {self.student.student_name}, Subject: {self.subject.subject_name}, Marks: {self.marks}'

    class Meta:
        unique_together = ['student','subject']
        verbose_name_plural = 'Marks'

'''-------------------------------------------------------------------------------------------------'''

class Report_Card(models.Model):
    student = models.ForeignKey(Student,related_name='stdt_report_card',on_delete=models.CASCADE)
    total = models.SmallIntegerField(null=True)
    rank = models.SmallIntegerField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Report Card'

'''-------------------------------------------------------------------------------------------------'''

# To test Aggregate and Annotate Functions.
class Customer(models.Model):
    Customer_Name = models.CharField(max_length=100)
    Customer_Age = models.SmallIntegerField(default = 0, null = True)

    def __str__(self) -> str:
        return f'Name: {self.Customer_Name}, Age: {self.Customer_Age}'

class Purchase(models.Model):
    Amount = models.IntegerField()
    Customer = models.ForeignKey(Customer,related_name='CP', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Name: {self.Customer.Customer_Name}, Amount: {self.Amount}'
    
'''-------------------------------------------------------------------------------------------------'''