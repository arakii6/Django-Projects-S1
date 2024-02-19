from faker import Faker
from .models import *
from django.db.models import Sum
import random

fake = Faker()

'''___________________________________________________________________________________'''
def create_marks():
    try:
        students = Student.objects.all()
        subjects = Subject.objects.all()
        
        for student in students:
            for subject in subjects:
                
                # Check if a Subject_Marks instance already exists for the student and subject
                existing_marks = Subject_Marks.objects.filter(student=student, subject=subject).exists()
                
                if not existing_marks:
                    # If no existing marks, create a new Subject_Marks instance
                    Subject_Marks.objects.create(
                        student = student,
                        subject = subject ,
                        marks = random.randint(30,100)
                    )
                else:
                    # Handle the case where an entry already exists (skip or update)
                    pass
                
    except Exception as e:
        print(e)

'''___________________________________________________________________________________'''
def fake_data(n):
    try:
        department_obj = Department.objects.all()
        for _ in range(n):
            # Create an instance of the Student Class
            Student.objects.create(
                department = random.choice(department_obj),
                studentid = StudentId.objects.create(student_id='STD' + str(random.randint(101,999))),
                student_name = fake.name(),
                student_email = fake.email(),
                student_age = random.randint(18,22),
                student_address = fake.address()
                )
        
        # Update the student_count attribute of Department Class
        queryset = Department.objects.all()
        for query in queryset:
            students = Student.objects.filter(department = query).count()
            query.student_count = students
            query.save()
    
    except Exception as e:
        print(e)

'''___________________________________________________________________________________'''
def report_card():

    '''Annotate function returns a the same queryset, 
    so here Ranks is a queryset(a Django specific data-type) and 
    student_marks_total is the total of each student's marks, in descending order.
    We can now loop throught Ranks and use .student_marks_total to check each individual
    student's total marks'''
    Ranks = Student.objects.annotate(
        student_marks_total = Sum('stdt_marks__marks')).order_by('-student_marks_total')
    
    i = 1
    for rank in Ranks:
        Report_Card.objects.create(
            student = rank,
            total = rank.student_marks_total,
            rank = i
        )
        i += 1

        '''
        In the above code, we have already created an queryset Rank which contains every student's total marks in
        descending order, so we can loop through Rank now and start assigning rank to every student.
        '''

'''___________________________________________________________________________________'''