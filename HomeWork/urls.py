from django.urls import path
from . import views

urlpatterns = [
    # Teachers
    path('teachers/', views.teacher_list_create, name='teacher-list-create'),  # GET list, POST create
    path('teachers/<int:pk>/', views.teacher_detail, name='teacher-detail-update-delete'),  # GET/PUT/DELETE one

    # Students
    path('students/', views.student_list_create, name='student-list-create'),
    path('students/<int:pk>/', views.student_detail, name='student-detail-update-delete'),

    # Assignments
    path('assignments/', views.assignment_list_create, name='assignment-list-create'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment-detail-update-delete'),

    # Student Submissions
    path('submissions/', views.submission_list_create, name='submission-list-create'),
    path('submissions/<int:pk>/', views.submission_detail, name='submission-detail-update-delete'),

    # Teacher Reviews
    path('reviews/', views.review_list_create, name='review-list-create'),
    path('reviews/<int:pk>/', views.review_detail, name='review-detail-update-delete'),
    
    
]
