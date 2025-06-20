from rest_framework import serializers
from .models import Teacher, Student, Assignment, StudentSubmission, TeacherReview

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

class StudentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSubmission
        fields = '__all__'

class TeacherReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherReview
        fields = '__all__'
