from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from .models import Teacher, Student, Assignment, StudentSubmission, TeacherReview
from .serializers import *

# --------------------- Teacher APIs ---------------------
@api_view(['GET', 'POST'])
def teacher_list_create(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def teacher_detail(request, pk):
    try:
        teacher = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found'})

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'DELETE':
        teacher.delete()
        return Response({'delete':'data deleted'})


# --------------------- Student APIs ---------------------
@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    if request.method == 'GET':
        return Response(StudentSerializer(student).data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=204)

# --------------------- Assignment APIs ---------------------
@api_view(['GET', 'POST'])
def assignment_list_create(request):
    if request.method == 'GET':
        assignments = Assignment.objects.all()
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def assignment_detail(request, pk):
    try:
        assignment = Assignment.objects.get(pk=pk)
    except Assignment.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    if request.method == 'GET':
        return Response(AssignmentSerializer(assignment).data)
    elif request.method == 'PUT':
        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        assignment.delete()
        return Response(status=204)

# --------------------- Student Submission APIs ---------------------
@api_view(['GET', 'POST'])
def submission_list_create(request):
    if request.method == 'GET':
        submissions = StudentSubmission.objects.all()
        serializer = StudentSubmissionSerializer(submissions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def submission_detail(request, pk):
    try:
        submission = StudentSubmission.objects.get(pk=pk)
    except StudentSubmission.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    if request.method == 'GET':
        return Response(StudentSubmissionSerializer(submission).data)
    elif request.method == 'PUT':
        serializer = StudentSubmissionSerializer(submission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        submission.delete()
        return Response(status=204)

# --------------------- Teacher Review APIs ---------------------
@api_view(['GET', 'POST'])

def review_list_create(request):
    if request.method == 'GET':
        reviews = TeacherReview.objects.all()
        serializer = TeacherReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TeacherReviewSerializer(data=request.data)

        if serializer.is_valid():
            try:
                review = serializer.save()
                submission = review.submission
                submission.status = 'Reviewed'
                submission.save()
                return Response(TeacherReviewSerializer(review).data, status=201)
            except Exception as e:
                return Response({'error': str(e)}, status=500)

        return Response(serializer.errors, status=400)



@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, pk):
    try:
        review = TeacherReview.objects.get(pk=pk)
    except TeacherReview.DoesNotExist:
        return Response({'error': 'Not Found'}, status=404)

    if request.method == 'GET':
        return Response(TeacherReviewSerializer(review).data)
    elif request.method == 'PUT':
        serializer = TeacherReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)


