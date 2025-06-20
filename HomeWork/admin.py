from django.contrib import admin

from .models import Teacher
from .models import Student
from .models import Assignment
from .models import StudentSubmission
from .models import TeacherReview

# Register your models here.

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(StudentSubmission)
admin.site.register(TeacherReview)
