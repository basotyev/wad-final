from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/create/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('courses/<int:course_id>/lessons/create/', views.create_lesson, name='create_lesson'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),

    path('courses/<int:course_id>/enroll/', views.enroll_in_course, name='enroll_in_course'),
    path('enrollments/', views.view_enrollments, name='view_enrollments'),
    path('courses/<int:course_id>/reviews/create/', views.create_review, name='create_review'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),
    path('courses/<int:course_id>/payment/', views.make_payment, name='make_payment'),
    path('payments/history/', views.payment_history, name='payment_history'),
    path('courses/<int:course_id>/quizzes/', views.quiz_list, name='quiz_list'),
    path('quizzes/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quizzes/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('progress/', views.view_progress, name='view_progress'),
]
