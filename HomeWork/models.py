from django.db import models

# Create your models here.
class Teacher(models.Model):
    id_no = models.CharField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    subject=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}({self.subject})"
    
    
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15,blank=True)
    course=models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True,primary_key=True)
    def __str__(self):
        return f"{self.name}({self.roll_number})"
    
class Assignment(models.Model):
    teacher= models.ForeignKey(Teacher,to_field='id_no',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    subject=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    due_date=models.DateField()
   
    description = models.CharField(max_length=255, blank=True, null=True)
    teacher_remark = models.TextField(blank=True) 
    pdf = models.FileField(upload_to='assignments/pdfs/', blank=True, null=True)
    def __str__(self):
        return self.title
    
class StudentSubmission(models.Model):
    student=models.ForeignKey('Student',to_field='roll_number',on_delete=models.CASCADE,related_name='submissions')
    assignment=models.ForeignKey('Assignment',on_delete=models.CASCADE,related_name='submissions')
    subject=models.CharField(max_length=200)
    submitted_file= models.FileField(upload_to='assignments/pdfs/', blank=True, null=True)
    STATUS_CHOICES = [
      
        ('Pending', 'Pending'),
        ('Submitted', 'Submitted'),
        ('Reviewed', 'Reviewed'), 
    
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at=models.DateField()
    student_remark=models.TextField(blank=True)
   
    def __str__(self):
        return f"{self.student.name} - {self.assignment.title} ({self.status})"
    
class TeacherReview(models.Model):
    submission=models.OneToOneField(StudentSubmission, on_delete=models.CASCADE,related_name='review')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)
    review_grade=models.CharField(max_length=10)
    teacher_review=models.CharField(max_length=100)
    reviewed_at=models.DateTimeField()

    def __str__(self):
        return f"Review by {self.teacher.name} for {self.submission}"
